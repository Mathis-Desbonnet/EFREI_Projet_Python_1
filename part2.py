import os
from TF_IDF_functions import IDFCalculator, TFCalculator
import math


def tokenQuestion(question: str):
    question = (
        question.replace("?", "")
        .replace(".", "")
        .replace(";", "")
        .replace(",", "")
        .replace(":", "")
        .replace("!", "")
        .replace("/", "")
        .replace("-", " ")
        .replace("'", " ")
        .replace('"', " ")
    )
    question = question.lower()
    return list(set(question.split())), question.split()


def getFilesWords(folderAddr: str):
    files = os.listdir(folderAddr)
    allWords = []
    for _ in files:
        text = open(folderAddr + _, "r").read()
        allWords += text.split()
        allWords = list(set(allWords))
    return allWords


def searchInteristingTerms(question: list, folderAddr: str):
    allWords = getFilesWords(folderAddr)
    interistingWord = []
    for word in question:
        if word in allWords:
            interistingWord.append(word)
    return interistingWord


def TFQuestion(question: list, folderAddr: str):
    allWords = getFilesWords(folderAddr)
    TFQuestion = {}
    for word in allWords:
        for wordQuestion in question:
            if word == wordQuestion:
                if word not in TFQuestion:
                    TFQuestion[word] = 1
                else:
                    TFQuestion[word] += 1
        if word not in TFQuestion:
            TFQuestion[word] = 0
    return TFQuestion


def TFIDFQuestion(question: list, folderAddr: str):
    TF = TFQuestion(question, folderAddr)
    IDF = IDFCalculator(folderAddr)

    TFIDFList = []
    for word in IDF.keys():
        TFIDFList.append(TF[word] * IDF[word])
    return TFIDFList, list(IDF.keys())


def TFIDFListPart2(folderAddr: str = "./cleaned/"):
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
    TFTab = (
        []
    )  # Create a list wich will be filled with dictionary using the TFCalculator function
    IDF = IDFCalculator(folderAddr)
    for fileName in os.listdir(folderAddr):  # Iterate though the files in the folder
        TFTab.append(TFCalculator(open(folderAddr + fileName, "r").read()))
    i = 0
    for numberOfFiles in range(len(os.listdir(folderAddr))):
        TFIDF.append([])
        for key in IDF.keys():
            if (
                key in TFTab[numberOfFiles].keys()
            ):  # Check if the word is in the TF dictionary
                TFIDF[i].append(IDF[key] * TFTab[numberOfFiles][key])
            else:
                TFIDF[i].append(None)
        i += 1
    return TFIDF, list(
        IDF.keys()
    )  # Return the TF-IDF list and the list of each unique words


print(TFIDFListPart2())


def produitScalaire(list1, list2):
    somme = 0
    for i in range(len(list1)):
        if list1[i] != None and list2[i] != None:
            somme += list1[i] * list2[i]
    return somme


def normeVecteur(list):
    normeSomme = 0
    for _ in list:
        if _ != None:
            normeSomme += _**2
    return math.sqrt(normeSomme)


def calculSimilarité(list1, list2):
    return produitScalaire(list1, list2) / (normeVecteur(list1) * normeVecteur(list2))


def bestDocument(TFIDFCorpus, TFIDFQuestion):
    max = 0
    maxIndex = 0
    for i in range(len(os.listdir("./cleaned/"))):
        temp = calculSimilarité(TFIDFQuestion, TFIDFCorpus[i])
        if temp >= max:
            maxIndex = i
            max = temp
    return os.listdir("./cleaned/")[maxIndex]


print(
    bestDocument(
        TFIDFListPart2()[0],
        TFIDFQuestion(
            tokenQuestion(
                "Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"
            )[1],
            "./cleaned/",
        )[0],
    )
)


print(
    tokenQuestion(
        "Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"
    )[0]
)

print(
    searchInteristingTerms(
        tokenQuestion(
            "Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"
        )[0],
        "./cleaned/",
    )
)

# print(
#     TFQuestion(
#         tokenQuestion(
#             "Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"
#         )[1],
#         "./cleaned/",
#     )
# )

print(
    TFIDFQuestion(
        tokenQuestion(
            "Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"
        )[1],
        "./cleaned/",
    )
)
