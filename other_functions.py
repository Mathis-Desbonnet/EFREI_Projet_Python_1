from TF_IDF_functions import TFCalculator, TFIDFList
import os
from fonctions import getPresidentNames

def IrreleventWords(matrice : list, WordsList : list) :
    '''
    Return the list of the irrelevents words (TD-IDF = 0)
    '''
    text = ""
    for indice in range(len(matrice)) :
        word = matrice[indice]
        val = True
        nbr = 0
        while (nbr < len(word)) and val :
            if word[nbr] != 0 :
                val = False
            nbr += 1
        text += (WordsList[indice] + "\n")*val
    text = text[:-1]
    return text

#print(IrreleventWords(TFIDFList()[0], TFIDFList()[1]))

def ImportantWords(matrice : list, WordsList : list) :
    '''
    Return the list of the importants words (high TD-IDF)
    '''
    maxTFIDF = 0
    WordsAndTFIDFScore = {}
    betterWords = []
    for i in range(len(matrice)) :
        maxTFIDFperWords = 0
        for j in range(len(matrice[i])) :
            if matrice[i][j] != None and matrice[i][j] > maxTFIDFperWords :
                maxTFIDFperWords += matrice[i][j]
        WordsAndTFIDFScore[WordsList[i]] = maxTFIDFperWords
        if maxTFIDF < maxTFIDFperWords :
            maxTFIDF = maxTFIDFperWords
    for key in WordsAndTFIDFScore.keys() :
        if WordsAndTFIDFScore[key] == maxTFIDF :
            betterWords.append(key)
    return betterWords

print(ImportantWords(TFIDFList()[0], TFIDFList()[1]))
print(TFIDFList()[0])

def ListOfWords(president : str, folderAdrr : str="./cleaned/") :
    '''
    Return a dictionnary of the words used by the chosen president (except the irrelevents words)
    '''
    dictio1 = {}
    Irrelevents = IrreleventWords(TFIDFList()[0], TFIDFList()[1])
    for fileName in os.listdir(folderAdrr):
        if president in fileName :
            dictio2 = TFCalculator(open(folderAdrr + fileName, "r").read())
            for keys in dictio2.keys() :
                if keys not in Irrelevents :
                    if keys in dictio1.keys() :
                        dictio1[keys] += dictio2[keys]
                    else :
                        dictio1[keys] = dictio2[keys]
    dictio1 = dict(sorted(dictio1.items(), key = lambda x : x[1], reverse = True))
    return dictio1


def MostUsedWords(president : str, folderAdrr : str="./cleaned/") :
    '''
    Return the list of the most used words by the chosen president
    '''
    dictio1 = ListOfWords(president, folderAdrr)
    text = ""
    for keys in list(dictio1.keys())[:10] :
        text += keys + "\n"
    text = text[:-1]
    return text


# print(MostUsedWords("Macron"))


def WhoTalkAbout(word : str, folderAdrr : str="./cleaned/") :
    '''
    Return the name of the president who talk about the word the most
    '''
    NamesList = getPresidentNames()
    PresidentsList = []
    for name in NamesList :
        if not name in PresidentsList :
            PresidentsList.append(name)
    HasTalkAbout = ""
    maxi = ["", 0]
    for president in PresidentsList :
        List = ListOfWords(president)
        if word in List.keys() :
            HasTalkAbout += president + "\n"
            if maxi[1] < List[word] :
                maxi = [president, List[word]]
    HasTalkAbout += "\n" + "Le président en ayant le plus parlé est : " + maxi[0]
    return HasTalkAbout
        
#print(WhoTalkAbout("nation"))


def FirstToSay(words : list) :
    '''
    Return the name of the president who talk about the words the first
    '''
    chronology = ["De Gaulle", "Pompidou", "Giscard", "Mitterrand", "Chirac", "Sarkozy", "Hollande", "Macron"]
    for president in chronology :
        List = ListOfWords(president)
        for word in words :
            if word in List.keys() :
                return president
            
# print(FirstToSay(["climat"]))


def UniversalWords() :
    '''
    Return the list of the words used by all the presidents
    '''
    List = TFIDFList()[0]
    Words = TFIDFList()[1]
    Irrelevents = IrreleventWords(List, Words)
    text = ""
    for i in range(len(List)) :
        val = True
        counter = 0
        # if Words[i] in Irrelevents :
        #     val = False
        while counter < len(List[i]) and val :
            if List[i][counter] == None :
                val = False
            counter += 1
        text += (Words[i] + "\n")*val
    text =  text[:-1]
    return text

print(UniversalWords())