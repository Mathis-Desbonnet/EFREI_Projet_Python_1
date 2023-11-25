from TF_IDF_functions import TFIDFList, occurrenceOfWords
import os
from fonctions import getPresidentNames


def irrelevantWords(matrice: list, wordsList: list):
    irrelevants = []
    for i in range(len(matrice)):
        word = matrice[i]
        isIrrelevant = True
        nbr = 0
        while (nbr < len(word)) and isIrrelevant:
            if word[nbr] != 0:
                isIrrelevant = False
            nbr += 1
        irrelevants += [wordsList[i]] * isIrrelevant
    return irrelevants


def importantWords(matrice: list, wordsList: list):
    maxTFIDF = 0
    wordsAndTFIDFScore = {}
    for i in range(len(matrice)):
        maxTFIDFperWords = 0
        for j in range(len(matrice[i])):
            if matrice[i][j] != None and matrice[i][j] > maxTFIDFperWords:
                maxTFIDFperWords = matrice[i][j]
        wordsAndTFIDFScore[wordsList[i]] = maxTFIDFperWords
        if maxTFIDF < maxTFIDFperWords:
            maxTFIDF = maxTFIDFperWords
    betterWords = []
    for key in wordsAndTFIDFScore.keys():
        if wordsAndTFIDFScore[key] == maxTFIDF:
            betterWords.append(key)
    return betterWords


def listOfWords(president: str, irrelevants: list, folderAddr: str):
    relevantUsedWords = []
    for fileName in os.listdir(folderAddr):
        if president in fileName:
            text = open(folderAddr + fileName, "r").read()
            allUsedWords = list(set(text.split()))
            for keys in allUsedWords:
                if keys not in irrelevants:
                    relevantUsedWords.append(keys)
    return relevantUsedWords


def mostUsedWords(president: str, irrelevants: list, folderAddr: str = "./cleaned/"):
    presidentWordsList = listOfWords(president, irrelevants, folderAddr)
    occurences = {}
    for word in presidentWordsList:
        nbr = 0
        for fileName in os.listdir(folderAddr):
            if president in fileName:
                nbr += occurrenceOfWords(open(folderAddr + fileName, "r").read(), word)
        occurences[word] = nbr
    sortedOccurences = sorted(occurences.items(), key=lambda x: x[1], reverse=True)
    mostUsedWords = list(map(lambda x: x[0], sortedOccurences[:10]))
    return mostUsedWords


def whoTalkAbout(word: str, irrelevants: list, folderAddr: str = "./cleaned/"):
    namesList = getPresidentNames()
    presidentsList = []
    for name in namesList:
        if not name in presidentsList:
            presidentsList.append(name)
    hasTalkAbout = []
    maxi = [
        "",
        0,
    ]
    for president in presidentsList:
        presidentWordsList = listOfWords(president, irrelevants, folderAddr)
        if word in presidentWordsList:
            hasTalkAbout.append(president)
            occurences = 0
            for fileName in os.listdir(folderAddr):
                if president in fileName:
                    occurences += occurrenceOfWords(
                        open(folderAddr + fileName, "r").read(), word
                    )
            if maxi[1] < occurences:
                maxi = [president, occurences]
    if hasTalkAbout == []:
        hasTalkAbout = "Nobody talked about this word..."
    else:
        hasTalkAbout.append("The president who talked the most about is : " + maxi[0])
    return hasTalkAbout


def firstToSay(words: list, irrelevants: list, folderAddr: str):
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
        presidentWordsList = listOfWords(president, irrelevants, folderAddr)
        for word in words:
            if word in presidentWordsList:
                return president
    return "Nobody talked about this word or maybe it's an irrelevant one..."


def universalWords(wordsList: list, irrelevants: list, folderAddr: str = "./cleaned/"):
    universals = []
    namesList = getPresidentNames()
    presidentWordsList = []
    for president in namesList:
        presidentWordsList.append(listOfWords(president, irrelevants, folderAddr))
    for word in wordsList:
        isUniversal = True
        counter = 0
        while isUniversal and counter < len(presidentWordsList):
            president = presidentWordsList[counter]
            if not word in president:
                isUniversal = False
            counter += 1
        universals += [word] * isUniversal
    if universals == []:
        return ["No important word has been used by all the presidents."]
    else:
        return universals
