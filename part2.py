import os
from TF_IDF_functions import IDFCalculator


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
    for word in TF.keys():
        TFIDFList.append(TF[word] * IDF[word])
    return TFIDFList


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
