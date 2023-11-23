import os


def getPresidentNames(folderAddr: str = "./speeches/"):
    """
    This function returns a list of French president's last names extracted from the filenames in a given folder.
    The function assumes that the files are named in the format "Nomination_{LastName}.txt".
    Any digits in the filenames are ignored.

    Parameters:
    folderAddr (str): The path to the folder containing the files. Defaults to "./speeches/".

    Returns:
    presidentsFileName (list): A list of strings containing the last names of French presidents.
    """

    presidentsFileName = os.listdir(folderAddr) # Get a list of all file names in the specified folder
    for i in range(len(presidentsFileName)):
        if ".txt" in presidentsFileName[i]: # Check if the file is a text file
            for chr in presidentsFileName[i]:
                if chr.isdigit(): # Check if the character is a digit
                    presidentsFileName[i] = presidentsFileName[i].replace(chr, "")
                presidentsFileName[i] = presidentsFileName[i].replace(".txt", "").replace("Nomination_", "") # Remove the text before and after the last name
    return presidentsFileName


def addPresidentSurname(listOfPresidents: list):
    """
    This function takes a list of French president's last names and returns a list of full names.
    It uses a predefined dictionary to map last names to first names.
    If a last name does not exist in the dictionary, it is returned as is.

    Parameters:
    listOfPresidents (list): A list of strings containing the last names of French presidents.

    Returns:
    presidentsWithSurname (list): A list of strings containing the full names of French presidents.
    """

    dictPresidents = { # Dictionary mapping last names to first names
        "Chirac": "Jacques Chirac",
        "Sarkozy": "Nicolas Sarkozy",
        "Hollande": "Francois Hollande",
        "Macron": "Emmanuel Macron",
        "Mitterrand": "Francois Mitterrand",
        "Giscard dEstaing": "Valerie Giscard dEstaing",
    }
    presidentsWithSurname = list(map(lambda x: dictPresidents[x] if x in dictPresidents else x, listOfPresidents))
    return presidentsWithSurname


def printPresidentNames(listOfPresidents: list):
    """
    This function prints the names of French presidents from a given list.
    Each president's name is printed only once, even if it appears multiple times in the list.

    Parameters:
    listOfPresidents (list): A list of strings containing the full names of French presidents.
    """

    arleadyPrinted = []
    for president in listOfPresidents:
        if president not in arleadyPrinted: # Check if the president's name has already been printed
            print(president)
            arleadyPrinted.append(president) # Add the president's name to the list of already printed names


def cleanPresidentText(speechFolderIn: str = "./speeches/", speechFolderOut: str = "./cleaned/"):
    """
    This function reads the text files from a given input folder, converts all uppercase letters to lowercase, 
    and writes the cleaned text to new files in a given output folder.
    The function only clean .txt files.

    Parameters:
    speechFolderIn (str): The path to the input folder containing the original text files. Defaults to "./speeches/".
    speechFolderOut (str): The path to the output folder where the cleaned text files will be written. Defaults to "./cleaned/".
    """
    os.mkdir(speechFolderOut, exist_ok=True) # Create the output folder if it does not exist
    fileName = os.listdir(speechFolderIn) # Get a list of all file names in the specified folder
    for file in fileName:
        if ".txt" in fileName: # Check if the file is a text file
            fileIn = open(speechFolderIn + file, "r")
            fileOut = open(speechFolderOut + file, "w")
            fileInLines = fileIn.readlines()
            for lignes in fileInLines: # Read the file line by line
                for char in lignes:
                    if ord(char) >= 65 and ord(char) <= 90: # Check if the character is an uppercase letter
                        fileOut.write(chr(ord(char) + 32)) # Convert the character to lowercase
                    else:
                        fileOut.write(char)
            fileIn.close()
            fileOut.close()


def deletePonctuationSign(cleanSpeechFolder: str = "./cleaned/"):
    """
    This function reads the text files from a given folder, removes punctuation marks, 
    and writes the cleaned text back to the same files. 
    The function only clean .txt files.

    Parameters:
    cleanSpeechFolder (str): The path to the folder containing the cleaned text files. Defaults to "./cleaned/".
    """

    fileName = os.listdir(cleanSpeechFolder) # Get a list of all file names in the specified folder
    for file in fileName:
        if ".txt" in fileName: # Check if the file is a text file
            fileOut = open(cleanSpeechFolder + file, "r")
            fileLines = fileOut.readlines()
            fileOut.close()
            fileOut = open(cleanSpeechFolder + file, "w")
            for lignes in fileLines: # Read the file line by line
                for char in lignes:
                    if char in ".,;:!?": # Check if the character is a punctuation mark
                        fileOut.write("") # Remove the punctuation mark
                    elif char in '''-'"''':
                        fileOut.write(" ") # Replace the punctuation mark wich are part of conpound words by a space
                    else:
                        fileOut.write(char)
            fileOut.close()
