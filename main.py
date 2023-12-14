import PySimpleGUI as sg # Import the library wich will be used to create the GUI.
import os
from fonctions import deletePonctuationSign, cleanPresidentText
import TF_IDF_functions as tfidf
import other_functions as of
import part2 as chatBot


sg.theme("DarkBlue12")
functionsList = [ # Create a list of all the functions the user can use.
    "irrelevantWords",
    "importantWords",
    "mostUsedWords",
    "whoTalkAbout",
    "firstToSay",
    "universalWords",
]

themesList = [ # Create a list of all the functions the user can use.
    "Pas de thème particulier",
    "Pas de pauvreté",
    "Faim zéro",
    "Bonne santé",
    "Éducation",
    "Égalité des sexes",
    "Eau propre",
    "Énergie propre",
    "Travail décent",
    "Industrie et innovation",
    "Inégalités réduites",
    "Villes durables",
    "Consommation responsable",
    "Changement climatique",
    "Vie aquatique",
    "Vie terrestre",
    "Paix et justice"
]

themeOfEachText = { # Create a dictionary wich associate each text to a theme
    "theme1" : [],
    "theme2" : []
}


path = ""

layout1 = [ # Create the layout of the first window.
    [sg.InputText(size=(20, 1), default_text=path, k="AddrInput"), sg.Text("Enter the directory path")], # Create the input where the user will enter the path and the text next to the input box.
    [sg.Combo(functionsList, k="FunctionInput"), sg.Text("Choose the function")], # Create the drop down list where the user will choose the function to use.
    [sg.Button("Change Mode"), sg.Text("Functions mode", key="textMode")],
    [sg.Button("Next Step")], #Create the button to go to the second window.
]
window1 = sg.Window("Main menu", layout1).Finalize()


def firstWindow(run, window): # Create the first window (the one where the user will enter the path and the function he wish to use).
    mode = "Functions mode"
    print("open first  window")
    while run: # The loop wich will keep the window open until the user close it or click on the "Next Step" button.
        event, values = window.read() # Get the event and the values of the window.

        if event in ("Close Window"): # Check if the user closed the window.
            run = False

        if event in ("Change Mode") :
            if mode == "Functions mode" :
                mode = "Chatbot mode"
                window['FunctionInput'].update(values=themesList)
            else :
                mode = "Functions mode"
                window['FunctionInput'].update(values=functionsList)
            window['textMode'].update(mode)

        if ( # Check if the user has entered a path and a function before clicking on the "Next Step" button.
            event in ("Next Step")
            and values["FunctionInput"] != ""
            and values["AddrInput"] != ""
        ):
            path = "./" + values["AddrInput"] + "/"
            function = values["FunctionInput"]

            if os.path.exists(path) == False: # Checl if the path entered by the user exist.
                layout3 = [[sg.Text("Path doesn't exist")]] # If not, create an error window.
                window3 = sg.Window("ErrorPath", layout3, keep_on_top=True).Finalize()

                run = False
                window.close()
                ErrorWindow(True, window3)
            else:
                if mode == "Functions Mode" :
                    if values["FunctionInput"] in ["whoTalkAbout", "firstToSay", "mostUsedWords"]:
                        layout2 = [ # Create the second window with an input box for the argument if the function the user wish to use require one.
                            [sg.InputText(size=(20, 1), k="ArgumentInput"), sg.Text("Enter the arguments")],
                            [sg.Multiline(size=(40, 20), disabled=True, key="Output")],
                            [sg.Button("Go"), sg.Push(), sg.Button("Previous")],
                        ]
                    else:
                        layout2 = [ # Create the second window without an input box for the argument if the function the user wish to use doesn't require one.
                            [sg.Push(), sg.Multiline(size=(40, 20), disabled=True, key="Output")],
                            [sg.Button("Go"), sg.Push(), sg.Button("Previous")],
                        ]
                else :
                    layout2 = [ # Create the second window with an input box for the argument if the function the user wish to use require one.
                            [sg.Multiline(size=(40, 20), disabled=True, key="Output")],
                            [sg.Text("Ask your question")],
                            [sg.InputText(size=(40, 1), k="ArgumentInput")],
                            [sg.Button("Go"), sg.Push(), sg.Button("Previous")]
                        ]

                run = False
                window.close()
                LoadingWindow(True, layout2, path, function)


def LoadingWindow(run, layout2, path, function): # Create a loading window (the one that will be displayed while the program is creating all the needed variables).
    cleanPresidentText(path)
    pathCleaned = path[:-1] + "_cleaned/"
    deletePonctuationSign(pathCleaned)
    layout4 = [[sg.Text("Chargement.....")]]
    window4 = sg.Window("LoadingWindow", layout4, keep_on_top=True).Finalize()
    event, values = window4.read(100)
    tfidfScore = tfidf.TFIDFList(pathCleaned)[0]
    tfidfWords = tfidf.TFIDFList(pathCleaned)[1]
    irrelevants = of.irrelevantWords(tfidfScore, tfidfWords)
    while run:
        window2 = sg.Window("Functions", layout2).Finalize()
        Output = window2.find_element("Output")
        run = False
        window4.close()
        secondWindow( # Launch the second window and create all the variables needed.
            True,
            window2,
            layout2,
            Output,
            path,
            pathCleaned, # The path to the directory, entered by the user in the first window.
            function, # The function the user want to use, entered by the user in the first window.
            tfidfScore, # The list of the TFIDF scores, create by using TFIDFList function.
            tfidfWords, # The list of the words, create by using TFIDFList function.
            irrelevants, # The list of the irrelevants words, create by using irrelevantWords function.
        )


def secondWindow(run, window, layout, Output, path, pathCleaned, functions, tfidfScore, tfidfWords, irrelevants):
    while run:
        event, values = window.read()
        if len(layout) >= 3:
            argument = values["ArgumentInput"]
        if event in ("Close Window"):
            run = False
            window.close()
        if event == "Go":
            Output.Update(disabled=False) # Allow to write in the output box.
            match functions: # Check wich function have to be used and use the functions of the other_functions.py file.
                case "irrelevantWords":
                    output = irrelevants
                case "importantWords":
                    output = of.importantWords(tfidfScore, tfidfWords)
                case "mostUsedWords":
                    output = of.mostUsedWords(argument, irrelevants, pathCleaned)
                case "whoTalkAbout":
                    output = of.whoTalkAbout(argument, irrelevants, pathCleaned)
                case "firstToSay":
                    argument = argument.split()
                    output = of.firstToSay(argument, irrelevants, pathCleaned)
                case "universalWords":
                    output = of.universalWords(tfidfWords, irrelevants, pathCleaned)

                case "Pas de thème particulier":
                    output = chatBot.betterAnswer(
                        chatBot.getSentence(
                            chatBot.getMaxTFIDFQuestion(
                                chatBot.TFIDFQuestion(
                                    chatBot.tokenQuestion(argument)[1],
                                    pathCleaned,
                                )[0],
                                chatBot.TFIDFQuestion(
                                    chatBot.tokenQuestion(argument)[1],
                                    pathCleaned,
                                )[1],
                            ),
                            chatBot.bestDocument(
                                chatBot.TFIDFListPart2(pathCleaned)[0],
                                chatBot.TFIDFQuestion(
                                    chatBot.tokenQuestion(argument)[1],
                                    pathCleaned,
                                )[0],
                                pathCleaned
                            ),
                        ),
                        argument
                    )

            Output.Update("")
            if type(output) == list: # Iterate tough the output if it's a list to display it in the output box.
                for i in output:
                    Output.Update(i + "\n", append=True)
            else:
                Output.Update(output) # Display the output in the output box if it's just a string.
            Output.Update(disabled=True)
        if event in ("Previous"): # Go back to the first window if the user click on the "Previous" button.
            run = False
            window.close()
            layout1 = [
                [sg.InputText(size=(20, 1), default_text=path[2:-1], k="AddrInput"), sg.Text("Enter the directory path")],
                [sg.Combo(functionsList, k="FunctionInput"), sg.Text("Choose the function")],
                [sg.Button("Change Mode"), sg.Text("Functions mode", key="textMode")],
                [sg.Button("Next Step")]
            ]
            window1 = sg.Window("Main menu", layout1).Finalize()
            firstWindow(True, window1) # Reopen the first window.


def ErrorWindow(run, window): # Create the error window (the one that will be displayed if the user enter a wrong path)
    while run:
        event, values = window.read()
        if event in ("Close Window"):
            run = False


run = True

firstWindow(run, window1) # The program starts here
