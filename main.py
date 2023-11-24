import PySimpleGUI as sg # Import the library we used to create the GUI
import os
import TF_IDF_functions as tfidf
import other_functions as of


sg.theme('DarkBlue12') # Set the theme of the GUI (color set)
comboList = ['irrelevantWords', 'importantWords', 'mostUsedWords', 'whoTalkAbout', 'firstToSay', 'universalWords'] # The list of functions
path = ""

run = True
while run : # The main loop to refrech the GUI
    layout1 = [  [sg.InputText(size=(20, 1), default_text=path, k="AddrInput"), sg.Text("Enter the directory path")], # The layout of the first window
                [sg.Combo(comboList, k="FunctionInput"), sg.Text("Choose the function")],
                [sg.Button('Next Step')],
            ]
    window1 = sg.Window('main', layout1).Finalize()

    run1 = True
    while run1: # The loop wich refresh the first window (the window wich ask the user to enter the path and the function)
        event, values = window1.read()
        
        if event in ('Close Window'): # If the user close the window
            run1, run = False

        if event in ('Next Step') and values["FunctionInput"] != "" and values["AddrInput"] != "": # Check if all fields are filled if the user clic on "Next Step"

            path = values["AddrInput"]
            function = values["FunctionInput"]

            if os.path.exists(path) == False:
                layout3 = [  [sg.Text("Path doesn't exist")]
                        ]
                window3 = sg.Window('ErrorPath', layout3, keep_on_top=True).Finalize()

                run1 = False
                run2 = False
                run3 = True
                window1.close()
            else:
                if values["FunctionInput"] in ["whoTalkAbout", "firstToSay", "mostUsedWords"]:
                    layout2 = [[sg.InputText(size=(20, 1), k="ArgumentInput"), sg.Text("Enter the arguments")], 
                            [sg.Multiline(size=(40, 20), disabled=True, key="Output")],
                            [sg.Button('Go'), sg.Push(), sg.Button('Previous')]]
                else:
                    layout2 = [[sg.Push(), sg.Multiline(size=(40, 20), disabled=True, key="Output")],
                            [sg.Button('Go'), sg.Push(), sg.Button('Previous')]]
                window2 = sg.Window('next', layout2).Finalize()
                Output = window2.find_element("Output")

                tfidfScore = tfidf.TFIDFList(path)[0]
                tfidfWords = tfidf.TFIDFList(path)[1]
                irrelevants = of.irrelevantWords(tfidfScore, tfidfWords)

                run1 = False
                run2 = True
                run3 = False
                window1.close()

    while run2: #the loop wich refresh the second window (the window wich display the result)
        event, values = window2.read()
        if len(layout2) == 3:
            argument = values["ArgumentInput"]
        if event in ('Close Window'):
            run2, run = False
            window2.close()
        if event == "Go":
            Output.Update(disabled=False)
            match function: 
                case "irrelevantWords": output = irrelevants
                case "importantWords": output = of.importantWords(tfidfScore, tfidfWords)
                case "mostUsedWords": output = of.mostUsedWords(argument, irrelevants, path)
                case "whoTalkAbout": output = of.whoTalkAbout(argument, path)
                case "firstToSay":
                    argument = argument.split()
                    output = of.firstToSay(argument, irrelevants, path)
                case "universalWords": output = of.universalWords(tfidfWords, irrelevants, path)
            Output.Update("")
            if type(output) == list:
                for i in output:
                    Output.Update(i + "\n", append=True)
            else : Output.Update(output)
            Output.Update(disabled=True)
        if event in ('Previous'):
            run1 = False
            run2 = False
            run3 = False
            window2.close()

    while run3: # The loop wich refresh the third window (path error window)
        event, values = window3.read()
        if event in ('Close Window'):
            run3, run = False