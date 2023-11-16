from TF_IDF_functions import TFCalculator, TFIDFList
import os
from fonctions import getPresidentNames


def irrelevantWords(matrice: list, wordsList: list):
    """
    Return a string wich contains the irrelevants words (TD-IDF = 0)
    """
    irrelevants = ""
    for i in range(len(matrice)):
        word = matrice[i]
        isImportant = True
        nbr = 0
        while (nbr < len(word)) and isImportant:
            if word[nbr] != 0:
                isImportant = False
            nbr += 1
        irrelevants += (wordsList[i] + "\n") * isImportant
    irrelevants = irrelevants[:-1]
    return irrelevants


# print(irrelevantWords(TFIDFList("./test/")[0], TFIDFList("./test/")[1]))
# print()


def importantWords(matrice: list, wordsList: list):
    """
    Return a string wich contains the importants words (high TD-IDF)
    """
    maxTFIDF = 0
    wordsAndTFIDFScore = {}
    betterWords = ""
    for i in range(len(matrice)):
        maxTFIDFperWords = 0
        for j in range(len(matrice[i])):
            if matrice[i][j] != None and matrice[i][j] > maxTFIDFperWords:
                maxTFIDFperWords += matrice[i][j]
        wordsAndTFIDFScore[wordsList[i]] = maxTFIDFperWords
        if maxTFIDF < maxTFIDFperWords:
            maxTFIDF = maxTFIDFperWords
    for key in wordsAndTFIDFScore.keys():
        if wordsAndTFIDFScore[key] == maxTFIDF:
            betterWords += key + "\n"
    betterWords = betterWords[:-1]
    return betterWords


# print(TFIDFList("./test/")[0], TFIDFList("./test/")[1])
# print(importantWords(TFIDFList("./test/")[0], TFIDFList("./test/")[1]))


def listOfWords(president : str, folderAddr : str="./cleaned/") :
    '''
    Return a dictionnary with the words used by the chosen president (except the irrelevants words)
    '''
    relevantUsedWords = []
    irrelevants = irrelevantWords(TFIDFList()[0], TFIDFList()[1])
    for fileName in os.listdir(folderAddr):
        if president in fileName :
            text = open(folderAddr + fileName, "r").read()
            allUsedWords = list(set(text.split()))
            for keys in allUsedWords :
                if keys not in irrelevants :
                        relevantUsedWords.append(keys)
    return relevantUsedWords

#print(listOfWords("Macron"))



def mostUsedWords(president: str, folderAddr: str = "./cleaned/"):
    """
    Return a string wich contains the most used words by the chosen president
    """
    presidentWordsList = listOfWords(president, folderAddr)
    mostUsedWords = ""
    for keys in list(presidentWordsList)[:10]:
        mostUsedWords += keys + "\n"
    mostUsedWords = mostUsedWords[:-1]
    return mostUsedWords


# print(mostUsedWords("Macron"))


def whoTalkAbout(word: str, folderAddr: str = "./cleaned/"):
    """
    Return the names of the presidents who has talked about a chosen word and the name of the president who has talked the most about it
    """
    namesList = getPresidentNames()
    presidentsList = []
    for name in namesList:
        if not name in presidentsList:
            presidentsList.append(name)
    hasTalkAbout = ""
    maxi = ["", 0]
    for president in presidentsList:
        presidentWordsList = listOfWords(president)
        if word in presidentWordsList:
            hasTalkAbout += president + "\n"
            if maxi[1] < presidentWordsList[word]:
                maxi = [president, presidentWordsList[word]]
    hasTalkAbout += "\n" + "The president who has talked the most about is : " + maxi[0]
    return hasTalkAbout


# print(whoTalkAbout("nation"))


def firstToSay(words: list):
    """
    Return the name of the president who has talked about the words the first
    """
    chronology = [
        "De Gaulle",
        "Pompidou",
        "Giscard",
        "Mitterrand",
        "Chirac",
        "Sarkozy",
        "Hollande",
        "Macron",
    ]
    for president in chronology:
        presidentWordsList = listOfWords(president)
        for word in words:
            if word in presidentWordsList:
                return president


# print(firstToSay(["climat"]))


def universalWords(wordsList: list, folderAddr: str = "./cleaned/"):
    """
    Return a string wich contains the words used by all the presidents (except the irrelevants words)
    """
    universals = ""
    namesList = getPresidentNames()
    irelevants = irrelevantWords(TFIDFList()[0], TFIDFList()[1])
    presidentWordsList = []
    for president in namesList:
        presidentWordsList.append(listOfWords(president))
    for word in wordsList:
        if not word in irelevants:
            val = True
            counter = 0
            while val and counter < len(presidentWordsList) :
                president = presidentWordsList[counter]
                if not word in president :
                    val = False
                counter += 1
            universals += (word + "\n")*val
    if universals == "" :
        return "No important word has been used by all the presidents."
    else : return universals


print()
print(universalWords(TFIDFList()[1]))
