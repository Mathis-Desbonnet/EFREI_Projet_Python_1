import os
import math

def occurrenceOfWords(text : str, word : str):
    """
    Returns the number of occurrences of a word in a text.
    """
    words = text.split()
    counter = 0
    for i in words:
        if i == word:
            counter += 1
    return counter

def TFCalculator(text : str):
    """
    Returns the term frequency of each word in a text.
    """
    words = text.split()
    words = list(set(words))
    TF = {}
    for word in words:
        TF[word] = occurrenceOfWords(text, word)
    return TF

def IDFCalculator(folderAddr : str="./cleaned/"):
    filesName = os.listdir(folderAddr)
    allWords = []
    for name in filesName:
        speechFile = open(folderAddr + name)
        text = speechFile.read()
        words = list(set(text.split()))
        allWords.append(words)

    IDF = {}
    while allWords != []:
        word = allWords[0][0]
        IDF[word] = 1
        for index in range(1, len(allWords)):
            if word in allWords[index]:
                allWords[index].remove(word)
                IDF[word] += 1
        allWords[0].remove(word)
        if allWords[0] == []:
            allWords.pop(0)

    for key in IDF.keys():
        IDF[key] = round(math.log10((len(filesName)/IDF[key])), 16)

    return IDF



def TFIDFList(folderAddr : str="./cleaned/"):
    TFIDF = []
    TFTab = []
    IDF = IDFCalculator(folderAddr)
    for fileName in os.listdir(folderAddr):
        TFTab.append(TFCalculator(open(folderAddr + fileName, "r").read()))
    i = 0
    for key in IDF.keys():
        TFIDF.append([])
        for numberOfFiles in range(len(os.listdir(folderAddr))):
            if key in TFTab[numberOfFiles].keys():
                TFIDF[i].append(IDF[key]*TFTab[numberOfFiles][key])
            else:
                TFIDF[i].append(None)
        i += 1
    
    return TFIDF, list(IDF.keys())

def printTab2D(listOfTFIDF : list):
    for i in range(len(listOfTFIDF)):
        for j in listOfTFIDF[i]:
            if j == 0.0:
                print(j, end="                ")
            elif type(j) == float:
                print(j, end=" ")
            elif j == None:
                print(j, end="               ")
        print()
    


#print(TFCalculator(open("./cleaned/Nomination_Chirac1.txt", "r").read()))
# IDFCalculator()