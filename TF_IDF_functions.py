import os
import math


def occurrenceOfWords(text: str, word: str):
    """
    This function returns the number of occurrences of a specific word in a given text.
    The text is split into words using spaces as delimiters.

    Parameters:
    text (str): The text in which we will count the occurrences of the word.
    word (str): The word to count occurences of.

    Returns:
    counter (int): The number of occurrences of the word in the text.
    """

    words = text.split() # Split the text into words using spaces as delimiters
    counter = 0
    for i in words:
        if i == word:
            counter += 1
    return counter


def TFCalculator(text: str):
    """
    This function calculates the TF (term Frequencie) of each unique word in a given text.
    The text is split into words using spaces as delimiters.
    The term frequency is the number of times a word appears in the text divided by the total number of words.

    Parameters:
    text (str): The text in which we will calculate the TF.

    Returns:
    TF (dict): A dictionary where the keys are the unique words and the values are their corresponding TF.
    """
    
    words = text.split()
    words = list(set(words)) # Remove duplicates words
    TF = {}
    for word in words:
        TF[word] = occurrenceOfWords(text, word) # Put the number of occurrences of each word in a dictionary
    return TF


def IDFCalculator(folderAddr: str = "./cleaned/"):
    """
    This function calculates the IDF (Inverse Document Frenquency) for each unique word across all text files in a given folder.
    The IDF is the logarithm of the total number of files divided by the number of files that contain the word.

    Parameters:
    folderAddr (str): The path to the folder containing the text files. Defaults to "./cleaned/".

    Returns:
    IDF (dict): A dictionary where the keys are the unique words and the values are their corresponding IDF.
    """

    filesName = os.listdir(folderAddr) # Get a list of all file names in the specified folder
    allWords = []
    for name in filesName: # Iterate though the files in the folder
        speechFile = open(folderAddr + name)
        text = speechFile.read()
        words = list(set(text.split())) # Put unique words of the text in a list
        allWords.append(words)

    IDF = {}
    while allWords != []:
        word = allWords[0][0]
        IDF[word] = 1
        for index in range(1, len(allWords)):
            if word in allWords[index]: # Check if the word is in the file matching with the index
                allWords[index].remove(word)
                IDF[word] += 1 # Increment the IDF value of the word if he is in the file
        allWords[0].remove(word)
        if allWords[0] == []:
            allWords.pop(0) # Remove the file if it is empty

    for key in IDF.keys(): # Iterate though the words in the IDF dictionary
        IDF[key] = round(math.log10((len(filesName) / IDF[key])), 16) # Apply the formula of the IDF on each words

    return IDF


def TFIDFList(folderAddr : str="./cleaned/"):
    """
    This function calculates the TF-IDF for each unique word across all text files in a given folder.
    The TF-IDF is the product of the TF and the IDF.

    Parameters:
    folderAddr (str): The path to the folder containing the text files. Defaults to "./cleaned/".

    Returns:
    TFIDF (list): A 2D list where each sublist corresponds to a unique word and contains the TF-IDF values for that word across all files.
    IDF.keys() (list): A list of all unique words.
    """

    TFIDF = []
    TFTab = [] # Create a list wich will be filled with dictionary using the TFCalculator function
    IDF = IDFCalculator(folderAddr)
    for fileName in os.listdir(folderAddr): # Iterate though the files in the folder
        TFTab.append(TFCalculator(open(folderAddr + fileName, "r").read()))
    i = 0
    for key in IDF.keys(): # Iterate though the words in the IDF dictionary
        TFIDF.append([])
        for numberOfFiles in range(len(os.listdir(folderAddr))):
            if key in TFTab[numberOfFiles].keys(): # Check if the word is in the TF dictionary
                TFIDF[i].append(IDF[key] * TFTab[numberOfFiles][key])
            else:
                TFIDF[i].append(None)
        i += 1
    return TFIDF, list(IDF.keys()) # Return the TF-IDF list and the list of each unique words


def printTab2D(listOfTFIDF: list):
    """
    This function prints a 2D list of TF-IDF values.
    Each sublist is printed on a new line.
    If a value is 0.0, it is printed with extra spaces for alignment.

    Parameters:
    listOfTFIDF (list): A 2D list of TF-IDF values.
    """
    for i in range(len(listOfTFIDF)):
        for j in listOfTFIDF[i]:
            if j == 0.0:
                print(j, end="                ")
            elif type(j) == float:
                print(j, end=" ")
            elif j == None:
                print(j, end="               ")
        print()