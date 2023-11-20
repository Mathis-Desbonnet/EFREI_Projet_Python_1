import PySimpleGUI as sg
import os
import TF_IDF_functions as tfidf
import other_functions as of


sg.theme('DarkBlue12')
comboList = ['irrelevantWords', 'importantWords', 'mostUsedWords', 'whoTalkAbout', 'firstToSay', 'universalWords']
layout1 = [  [sg.InputText(size=(20, 1), k="AddrInput"), sg.Text("Enter the directory path")],
            [sg.Combo(comboList, k="FunctionInput"), sg.Text("Choose the function")],
            [sg.Button('Next Step')],
        ]
window1 = sg.Window('main', layout1).Finalize()
run = True

while run:
    event, values = window1.read()
    
    if event in ('Close Window'):
        run = False

    if event in ('Next Step') and values["FunctionInput"] != "" and values["AddrInput"] != "":

        path = values["AddrInput"]
        function = values["FunctionInput"]

        if os.path.exists(path) == False:
            layout3 = [  [sg.Text("Path doesn't exist")]
                    ]
            window3 = sg.Window('ErrorPath', layout3, keep_on_top=True).Finalize()

            run = False
            run2 = False
            run3 = True
            window1.close()
        else:
            if values["FunctionInput"] == "whoTalkAbout" or values["FunctionInput"] == "firstToSay":
                layout2 = [[sg.InputText(size=(20, 1)), sg.Text("Enter the arguments")], 
                        [sg.Multiline(size=(40, 20), disabled=True, key="Output")],
                        [sg.Button('Go')]]
            else:
                layout2 = [[sg.Push(), sg.Multiline(size=(40, 20), disabled=True, key="Output")],
                        [sg.Button('Go')]]
            window2 = sg.Window('next', layout2).Finalize()
            Output = window2.FindElement("Output")
            tfidfScore = tfidf.TFIDFList(path)[0]
            tfidfWords = tfidf.TFIDFList(path)[1]

            run = False
            run2 = True
            run3 = False
            window1.close()

while run2:
    event, values = window2.read()
    if event in ('Close Window'):
        run2 = False
        window2.close()
    if event == "Go":
        Output.Update(disabled=False)
        match function: 
            case "irrelevantWords": Output.Update(of.irrelevantWords(tfidfScore, tfidfWords))
            case "importantWords": Output.Update(of.importantWords(tfidfScore, tfidfWords))
            #case "mostUsedWords": Output.Update(of.mostUsedWords(argument, path))
            #case "whoTalkAbout": Output.Update(of.whoTalkAbout(argument, path))
            #case "firstToSay": Output.Update(of.firstToSay(argument))
            case "irrelevantWords": Output.Update(of.irrelevantWords(tfidfScore, tfidfWords))
        Output.Update(disabled=True)

while run3:
    event, values = window3.read()
    if event in ('Close Window'):
        run3 = False
        window3.close()