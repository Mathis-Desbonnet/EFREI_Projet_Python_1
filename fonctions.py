import os

def getPresidentNames(folderAdrr : str="./speeches/"):
    """Returns a list of presidents names"""
    presidentsFileName = os.listdir(folderAdrr)
    for i in range(len(presidentsFileName)):
        for chr in presidentsFileName[i]:
            if chr.isdigit():
                presidentsFileName[i] = presidentsFileName[i].replace(chr, "")
        presidentsFileName[i] = presidentsFileName[i].replace(".txt", "").replace("Nomination_", "")
    return presidentsFileName

def addPresidentSurname(listOfPresidents : list):
    dictPresidents = {"Chirac": "Jacques Chirac", "Sarkozy": "Nicolas Sarkozy", "Hollande": "Francois Hollande", "Macron": "Emmanuel Macron", "Mitterrand":"Francois Mitterrand", "Giscard dEstaing":"Valerie Giscard dEstaing"}
    presidentsWithSurname = list(map(lambda x: dictPresidents[x] if x in dictPresidents else x, listOfPresidents))
    return presidentsWithSurname

def printPresidentNames(listOfPresidents : list):
    """Prints the list of presidents names"""
    arleadyPrinted = []
    for president in listOfPresidents:
        if president not in arleadyPrinted:
            print(president)
            arleadyPrinted.append(president)

def cleanPresidentText(speechFolderIn : str="./speeches/", speechFolderOut : str="./cleaned/"):
    fileName = os.listdir(speechFolderIn)
    for file in fileName:
        fileIn = open(speechFolderIn+file, "r")
        fileOut = open(speechFolderOut+file, "w")
        fileInLines = fileIn.readlines()
        for lignes in fileInLines:
            for char in lignes:
                if 65 <= ord(char) and ord(char) <= 90:
                    fileOut.write(chr(ord(char)+32))
                else:
                    fileOut.write(char)
        fileIn.close()
        fileOut.close()
    return "done"

def deletePonctuationSign(cleanSpeechFolder : str="./cleaned/"):
    fileName = os.listdir(cleanSpeechFolder)
    for file in fileName:
        fileOut = open(cleanSpeechFolder+file, "r")
        fileLines = fileOut.readlines()
        fileOut.close()
        fileOut = open(cleanSpeechFolder+file, "w")
        for lignes in fileLines:
            for char in lignes:
                if char in ".,;:!?":
                    fileOut.write("")
                elif char in '''-'"''':
                    fileOut.write(" ")
                else:
                    fileOut.write(char)
        fileOut.close()
    return "done"

printPresidentNames(addPresidentSurname(getPresidentNames()))
print(cleanPresidentText())
print(deletePonctuationSign())