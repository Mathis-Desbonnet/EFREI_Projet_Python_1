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
        text = open(folderAddr + _, "r", encoding="utf-8").read()
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
    print(TFIDFList[list(IDF.keys()).index("climat")])
    print(TFIDFList[list(IDF.keys()).index("pourquoi")])
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
        TFTab.append(
            TFCalculator(open(folderAddr + fileName, "r", encoding="utf-8").read())
        )
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


# print(TFIDFListPart2())


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


def bestDocument(TFIDFCorpus, TFIDFQuestion, folderAddr):
    max = 0
    maxIndex = 0
    for i in range(len(os.listdir(folderAddr))):
        temp = calculSimilarité(TFIDFQuestion, TFIDFCorpus[i])
        if temp >= max:
            maxIndex = i
            max = temp
    print(os.listdir(folderAddr)[maxIndex])
    return os.listdir(folderAddr)[maxIndex]


def getMaxTFIDFQuestion(TFIDFQuestion, listQuestion):
    print(max(TFIDFQuestion))
    print(TFIDFQuestion.index(max(TFIDFQuestion)))
    print(listQuestion[TFIDFQuestion.index(max(TFIDFQuestion))])
    return listQuestion[TFIDFQuestion.index(max(TFIDFQuestion))]


def getSentence(maxTFIDFQuestion, bestDocument, path):
    print(maxTFIDFQuestion)
    file = open(path + bestDocument, "r", encoding="utf-8")
    sentences = file.read().split(".")
    for sentence in sentences:
        if maxTFIDFQuestion in sentence:
            return sentence


def betterAnswer(answer, question):
    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr! ",
    }

    firstQuestionWord = question.split()[0]
    if answer != None:
        answer = answer.replace("\n", "")
    else:
        return "Il n'y a pas de réponse à votre question dans les textes données...."
    if firstQuestionWord in question_starters:
        return question_starters[firstQuestionWord] + answer.lower() + "."
    else:
        return answer + "."


# question = input("Saisir la question : ")

# print(tokenQuestion(question)[0])

# print(
#     searchInteristingTerms(
#         tokenQuestion(question)[0],
#         "./cleaned/",
#     )
# )

# print(
#     TFQuestion(
#         tokenQuestion(
#             question
#         )[1],
#         "./cleaned/",
#     )
# )

# print(
#     TFIDFQuestion(
#         tokenQuestion(question)[1],
#         "./cleaned/",
#     )
# )

# print(
#     bestDocument(
#         TFIDFListPart2()[0],
#         TFIDFQuestion(
#             tokenQuestion(question)[1],
#             "./cleaned/",
#         )[0],
#     )
# )

# print(
#     getMaxTFIDFQuestion(
#         TFIDFQuestion(
#             tokenQuestion(question)[1],
#             "./cleaned/",
#         )[0],
#         TFIDFQuestion(
#             tokenQuestion(question)[1],
#             "./cleaned/",
#         )[1],
#     )
# )

# print(
#     betterAnswer(
#         getSentence(
#             getMaxTFIDFQuestion(
#                 TFIDFQuestion(
#                     tokenQuestion(question)[1],
#                     "./speeches_cleaned/",
#                 )[0],
#                 TFIDFQuestion(
#                     tokenQuestion(question)[1],
#                     "./speeches_cleaned/",
#                 )[1],
#             ),
#             bestDocument(
#                 TFIDFListPart2("./speeches_cleaned/")[0],
#                 TFIDFQuestion(
#                     tokenQuestion(question)[1],
#                     "./speeches_cleaned/",
#                 )[0],
#                 "./speeches_cleaned/",
#             ),
#             "./speeches/",
#         ),
#         question,
#     )
# )
