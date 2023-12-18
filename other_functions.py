from TF_IDF_functions import TFIDFList, occurrenceOfWords
import os
from fonctions import getPresidentNames


def irrelevantWords(matrice: list, wordsList: list):
    """
    This function returns a list which contains the irrelevant words from a given list of words.
    A word is considered irrelevant if all of his TF-IDF value are 0 in the given list.

    Parameters:
    matrice (list): A 2D list of TF-IDF values.
    wordsList (list): A list of words corresponding to the TF-IDF values in the matrix.

    Returns:
    irrelevants (list): A list of irrelevant words.
    """

    irrelevants = []
    for i in range(len(matrice)):
        word = matrice[i]
        isIrrelevant = True
        nbr = 0
        while (nbr < len(word)) and isIrrelevant:
            if word[nbr] != 0:  # Check if the word has a TF-IDF of 0.
                isIrrelevant = False  # Mark the word as not irrelevant.
            nbr += 1
        irrelevants += [
            wordsList[i]
        ] * isIrrelevant  # Add the word into the irrelevants if isIrrelevant is True.
    return irrelevants


def importantWords(matrice: list, wordsList: list):
    """
    This function returns a list which contains the important words from a given list of words.
    A word is considered important if its TF-IDF value is the highest in the given matrix.

    Parameters:
    matrice (list): A 2D list of TF-IDF values.
    wordsList (list): A list of words corresponding to the TF-IDF values in the matrix.

    Returns:
    betterWords (list): A list of important words.
    """

    maxTFIDF = 0
    wordsAndTFIDFScore = {}
    for i in range(
        len(matrice)
    ):  # Determine the highest TF-IDF value among the given values in "matrice".
        maxTFIDFperWords = 0
        for j in range(len(matrice[i])):
            if (
                matrice[i][j] != None and matrice[i][j] > maxTFIDFperWords
            ):  # Search the highest TF-IDF of the word across all the text.
                maxTFIDFperWords = matrice[i][j]
        wordsAndTFIDFScore[
            wordsList[i]
        ] = maxTFIDFperWords  # Match a word with his highest TF-IDF value in a dictionary.
        if maxTFIDF < maxTFIDFperWords:
            maxTFIDF = maxTFIDFperWords  # Update the highest TF-IDF value across all the words if a higher value is found.
    betterWords = []
    for key in wordsAndTFIDFScore.keys():
        if (
            wordsAndTFIDFScore[key] == maxTFIDF
        ):  # Check if the highest TF-IDF of each word is equal to the highest TF-IDF.
            betterWords.append(key)
    return betterWords


def listOfWords(president: str, irrelevants: list, folderAddr: str):
    """
    This function returns a list of unique words used by a specified president, excluding a given list of irrelevant words.
    The function reads the text files from a given folder, splits the text into words, and filters out the irrelevant words.
    This function is used by all the next functions wich require a list of all the words used by a specific president.

    Parameters:
    president (str): The name of the president.
    irrelevants (list): A list of irrelevant words to be excluded.
    folderAddr (str): The path to the folder containing the text files.

    Returns:
    relevantUsedWords (list): A list of the relevant words used by the president.
    """

    relevantUsedWords = []
    for fileName in os.listdir(
        folderAddr
    ):  # Iterate tough the files wich are in folderAddr
        if president in fileName:
            text = open(folderAddr + fileName, "r", encoding="utf-8").read()
            allUsedWords = list(
                set(text.split())
            )  # Put unique words of the text in a list
            for keys in allUsedWords:
                if keys not in irrelevants:  # Check if the word is not relevant
                    relevantUsedWords.append(keys)
    return relevantUsedWords


def mostUsedWords(president: str, irrelevants: list, folderAddr: str = "./cleaned/"):
    """
    This function returns a list which contains the most frequently used words by a specified president, excluding a given list of irrelevant words.
    The function use listOfWords() to get the list of relevant words used by the president.
    And then, counts the number of occurences of each word.

    Parameters:
    president (str): The name of the president.
    irrelevants (list): A list of irrelevant words to be excluded.
    folderAddr (str): The path to the folder containing the text files. Defaults to "./cleaned/".

    Returns:
    mostUsedWords (list): A list of the most frequently used words by the president, separated by newlines.
    """

    presidentWordsList = listOfWords(
        president, irrelevants, folderAddr
    )  # Create a list of all the words used by the given president.
    occurences = {}
    for word in presidentWordsList:
        nbr = 0
        for fileName in os.listdir(folderAddr):  # Iterate tough the files in folderAddr
            if president in fileName:
                nbr += occurrenceOfWords(
                    open(folderAddr + fileName, "r", encoding="utf-8").read(), word
                )
        occurences[word] = nbr
    sortedOccurences = sorted(
        occurences.items(), key=lambda x: x[1], reverse=True
    )  # Sort the words with their occurences.
    mostUsedWords = list(map(lambda x: x[0], sortedOccurences[:10]))
    # mostUsedWords = []
    # maxi = sortedOccurences[0][1]
    # continueLoop = True
    # _ = 0
    # while _ <= len(sortedOccurences) and continueLoop:
    #     mostUsedWords.append(sortedOccurences[_][0])
    #     _ += 1
    #     if sortedOccurences[_][1] < maxi:
    #         continueLoop = False
    return mostUsedWords


def whoTalkAbout(word: str, irrelevants: list, folderAddr: str = "./cleaned/"):
    """
    This function returns the names of the presidents who talked about a chosen word and the name of the president who has talked the most about it.
    The function use listOfWords() to get the list of relevant words used by each president.

    Parameters:
    word (str): The word to check.
    irrelevants (list): A list of irrelevant words to be excluded.
    folderAddr (str): The path to the folder containing the text files. Defaults to "./cleaned/".

    Returns:
    hasTalkAbout (list): A list of the names of the presidents who talked about the chosen word, and the name of the president who has talked the most about it.
    """

    namesList = getPresidentNames()  # Get a list of all president's names.
    presidentsList = []
    for name in namesList:  # Remove the duplicates of namesList
        if not name in presidentsList:
            presidentsList.append(name)
    hasTalkAbout = []
    maxi = [
        "",
        0,
    ]  # Create a list wich contain the name of the president who has talked the most about the word and the number of time he said the word.
    for president in presidentsList:
        presidentWordsList = listOfWords(
            president, irrelevants, folderAddr
        )  # Create a list of all the words used by the given president.
        if word in presidentWordsList:
            hasTalkAbout.append(president)
            occurences = 0
            for fileName in os.listdir(folderAddr):
                if president in fileName:
                    occurences += occurrenceOfWords(
                        open(folderAddr + fileName, "r", encoding="utf-8").read(), word
                    )
            if (
                maxi[1] < occurences
            ):  # Check if this president has talked more about this word than the president stored in "maxi"
                maxi = [president, occurences]
    if hasTalkAbout == []:  # Check if nobody has talked about this word.
        hasTalkAbout = "Nobody talked about this word..."
    else:
        hasTalkAbout.append(
            "The president who talked the most about is : " + maxi[0]
        )  # Add the name of the president who has talked the most about this word.
    return hasTalkAbout


def firstToSay(words: list, irrelevants: list, folderAddr: str):
    """
    This function returns the name of the president who first talked about at least one of the given words.
    The function use listOfWords() to get the list of relevant words used by each president.

    Parameters:
    words (list): The list of words to check.
    irrelevants (list): A list of irrelevant words to be excluded.
    folderAddr (str): The path to the folder containing the text files.

    Returns:
    president (str): The name of the president who first talked about the given words.
    """

    chronology = [  # Create a list filled with the presidents names sorted by chronological order.
        "De Gaulle",
        "Pompidou",
        "Giscard",
        "Mitterrand",
        "Chirac",
        "Sarkozy",
        "Hollande",
        "Macron",
    ]
    for president in chronology:  # Iterate tough the president list.
        presidentWordsList = listOfWords(president, irrelevants, folderAddr)
        for word in words:
            if (
                word in presidentWordsList
            ):  # Check if the president has talk about one of the words.
                return president
    return "Nobody talked about this word or maybe it's an irrelevant one..."


def universalWords(wordsList: list, irrelevants: list, folderAddr: str = "./cleaned/"):
    """
    This function returns a list which contains the words used by all the presidents, excluding a given list of irrelevant words.
    The function use listOfWords() to get the list of relevant words used by each president.
    And then, checks wich words has been used by all the presidents.

    Parameters:
    wordsList (list): The list of words to check.
    irrelevants (list): A list of irrelevant words to be excluded.
    folderAddr (str): The path to the folder containing the text files. Defaults to "./cleaned/".

    Returns:
    universals (list): A list of the words used by all the presidents.
    """
    universals = []
    namesList = getPresidentNames()  # Get a list of all president's names.
    presidentWordsList = (
        []
    )  # A list wich will contain all the words used by all the presidents
    for president in namesList:
        presidentWordsList.append(
            listOfWords(president, irrelevants, folderAddr)
        )  # Create a list of all the words used by the given president.
    for word in wordsList:
        isUniversal = True
        counter = 0
        while isUniversal and counter < len(presidentWordsList):
            president = presidentWordsList[counter]
            if not word in president:
                isUniversal = False
            counter += 1
        universals += [
            word
        ] * isUniversal  # Add the word into universals if isUniversal is True.
    if universals == []:
        return ["No important word has been used by all the presidents."]
    else:
        return universals
