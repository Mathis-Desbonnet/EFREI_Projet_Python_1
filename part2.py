import os
from TF_IDF_functions import IDFCalculator, TFCalculator
import math


def tokenQuestion(question: str):
    '''
    This function clean the asked question and return the list of each unique word of it.

    Parameters :
    question (str) : the asked question to clean

    Returns :
    token (list) : the list of each unique word in the question.
    '''

    question = (
        question.replace("?", "") # Clean the question by removing ponctuation marks.
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
    question = question.lower() # Convert question's uppercases into lowercases
    token = list(set(question.split())), question.split()
    return  # return the list of each unique word of the cleaned question.


def getFilesWords(folderAddr: str):
    """
    This function reads all the text files in a given folder and returns a list of unique words found in these files.

    Parameters:
    folderAddr (str): The path to the folder containing the text files.

    Returns:
    allWords (list): A list of unique words found in the text files.
    """

    files = os.listdir(folderAddr)
    allWords = []
    for _ in files:
        text = open(folderAddr + _, "r", encoding="utf-8").read()
        allWords += text.split()
        allWords = list(set(allWords))
    return allWords


def searchInterestingTerms(question: list, folderAddr: str):
    """
    This function returns a list of words from a given question that are found in the text files in a given folder.

    Parameters:
    question (list): The list of words from the question.
    folderAddr (str): The path to the folder containing the text files.

    Returns:
    interistingWord (list): A list of words from the question wich are found in the text files.
    """

    allWords = getFilesWords(folderAddr)
    interistingWord = []
    for word in question:
        if word in allWords:
            interistingWord.append(word)
    return interistingWord


def TFQuestion(question: list, folderAddr: str):
    """
    This function calculates the Term Frequency (TF) of each word in a given question.

    Parameters:
    question (list): The list of words from the question.
    folderAddr (str): The path to the folder containing the text files.

    Returns:
    TFQuestion (dict): A dictionary where the keys are the words and the values are the TFs.
    """

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
    """
    This function calculates the Term Frequency-Inverse Document Frequency (TF-IDF) of each word in a given question.

    Parameters:
    question (list): The list of words from the question.
    folderAddr (str): The path to the folder containing the text files.

    Returns:
    TFIDFList (list): A list of the TF-IDF values for each word in the question.
    IDF.keys() (list): A list of the words in the question.
    """

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
    """
    This function calculates and returns the scalar product of two vectors.
    The scalar product is the sum of the products of the corresponding entries of the two sequences of numbers.

    Parameters:
    list1 (list): The first vector.
    list2 (list): The second vector.

    Returns:
    somme (float): The scalar product of the two vectors
    """

    somme = 0
    for i in range(len(list1)):
        if list1[i] != None and list2[i] != None:
            somme += list1[i] * list2[i]
    return somme


def normeVecteur(list):
    """
    This function calculates and returns the Euclidean norm of a vector.

    Parameters:
    list (list): The vector.

    Returns:
    norm: The Euclidean norm of the vector.
    """
    
    normeSomme = 0
    for _ in list:
        if _ != None:
            normeSomme += _**2
    return math.sqrt(normeSomme)


def calculSimilarité(list1, list2):
    """
    This function calculates and returns the cosine similarity between two vectors.

    Parameters:
    list1 (list): The first vector.
    list2 (list): The second vector.

    Returns:
    similarity (float): The cosine similarity between the two vectors.
    """

    similarity = produitScalaire(list1, list2) / (normeVecteur(list1) * normeVecteur(list2))
    return similarity


def bestDocument(TFIDFCorpus, TFIDFQuestion, folderAddr):
    """
    This function calculates the similarity between the TF-IDF vectors of the question and each document in the corpus.

    Parameters:
    TFIDFCorpus (list): A list of the TF-IDF vectors for each document in the corpus.
    TFIDFQuestion (list): The TF-IDF vector for the question.
    folderAddr (str): The path to the folder containing the documents.

    Returns:
    file (str): The name of the file with the highest similarity score.
    """

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
    """
    This function finds and returns the word from the question that has the highest TF-IDF score.

    Parameters:
    TFIDFQuestion (list): A list of the TF-IDF scores for each word in the question.
    listQuestion (list): A list of the words in the question.

    Returns:
    highestTFIDF (str): The word from the question that has the highest TF-IDF score.
    """

    highestTFIDF = listQuestion[TFIDFQuestion.index(max(TFIDFQuestion))]
    return highestTFIDF


def getSentence(maxTFIDFQuestion, bestDocument, path):
    """
    This function returns the sentence from the best matching document that contains the word with the highest TF-IDF score.

    Parameters:
    maxTFIDFQuestion (str): The word from the question with the highest TF-IDF score.
    bestDocument (str): The name of the best matching document.
    path (str): The path to the folder containing the document.

    Returns:
    sentence (str): The sentence that contains the word with the highest TF-IDF score.
    """

    print(maxTFIDFQuestion)
    file = open(path + bestDocument, "r", encoding="utf-8")
    sentences = file.read().split(".") # Split the text into a list of sentences
    for sentence in sentences:
        if maxTFIDFQuestion in sentence:
            return sentence


def betterAnswer(answer, question):
    """
    This function improves the answer to a given question by adding a suitable response starter based on the first word of the question.
    If the answer is None, the function returns a default response.

    Parameters:
    answer (str): The answer to the question.
    question (str): The question.

    Returns:
    answer (str): The improved answer.
    """

    question_starters = { # Create a dictionary wich associate each question starter with an answer starter.
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