import PySimpleGUI as sg
import os
import TF_IDF_functions as tfidf
import other_functions as of


sg.theme("DarkBlue12")
comboList = [
    "irrelevantWords",
    "importantWords",
    "mostUsedWords",
    "whoTalkAbout",
    "firstToSay",
    "universalWords",
]
path = ""

layout1 = [
    [
        sg.InputText(size=(20, 1), default_text=path, k="AddrInput"),
        sg.Text("Enter the directory path"),
    ],
    [sg.Combo(comboList, k="FunctionInput"), sg.Text("Choose the function")],
    [sg.Button("Next Step")],
]
window1 = sg.Window("main", layout1).Finalize()


def firstWindow(run, window):
    print("open first  window")
    while run:
        event, values = window.read()

        if event in ("Close Window"):
            run = False

        if (
            event in ("Next Step")
            and values["FunctionInput"] != ""
            and values["AddrInput"] != ""
        ):
            path = values["AddrInput"]
            function = values["FunctionInput"]

            if os.path.exists(path) == False:
                layout3 = [[sg.Text("Path doesn't exist")]]
                window3 = sg.Window("ErrorPath", layout3, keep_on_top=True).Finalize()

                run = False
                window.close()
                ErrorWindow(True, window3)
            else:
                if values["FunctionInput"] in [
                    "whoTalkAbout",
                    "firstToSay",
                    "mostUsedWords",
                ]:
                    layout2 = [
                        [
                            sg.InputText(size=(20, 1), k="ArgumentInput"),
                            sg.Text("Enter the arguments"),
                        ],
                        [sg.Multiline(size=(40, 20), disabled=True, key="Output")],
                        [sg.Button("Go"), sg.Push(), sg.Button("Previous")],
                    ]
                else:
                    layout2 = [
                        [
                            sg.Push(),
                            sg.Multiline(size=(40, 20), disabled=True, key="Output"),
                        ],
                        [sg.Button("Go"), sg.Push(), sg.Button("Previous")],
                    ]

                run = False
                window.close()
                LoadingWindow(True, layout2, path, function)


def LoadingWindow(run, layout2, path, function):
    layout4 = [[sg.Text("Chargement.....")]]
    window4 = sg.Window("LoadingWindow", layout4, keep_on_top=True).Finalize()
    event, values = window4.read(100)
    tfidfScore = tfidf.TFIDFList(path)[0]
    tfidfWords = tfidf.TFIDFList(path)[1]
    irrelevants = of.irrelevantWords(tfidfScore, tfidfWords)
    while run:
        window2 = sg.Window("next", layout2).Finalize()
        Output = window2.find_element("Output")
        run = False
        window4.close()
        secondWindow(
            True,
            window2,
            layout2,
            Output,
            path,
            function,
            tfidfScore,
            tfidfWords,
            irrelevants,
        )


def secondWindow(
    run, window, layout, Output, path, functions, tfidfScore, tfidfWords, irrelevants
):
    while run:
        event, values = window.read()
        if len(layout) == 3:
            argument = values["ArgumentInput"]
        if event in ("Close Window"):
            run = False
            window.close()
        if event == "Go":
            Output.Update(disabled=False)
            match functions:
                case "irrelevantWords":
                    output = irrelevants
                case "importantWords":
                    output = of.importantWords(tfidfScore, tfidfWords)
                case "mostUsedWords":
                    output = of.mostUsedWords(argument, irrelevants, path)
                case "whoTalkAbout":
                    output = of.whoTalkAbout(argument, path)
                case "firstToSay":
                    argument = argument.split()
                    output = of.firstToSay(argument, irrelevants, path)
                case "universalWords":
                    output = of.universalWords(tfidfWords, irrelevants, path)
            Output.Update("")
            if type(output) == list:
                for i in output:
                    Output.Update(i + "\n", append=True)
            else:
                Output.Update(output)
            Output.Update(disabled=True)
        if event in ("Previous"):
            run = False
            window.close()
            layout1 = [
                [
                    sg.InputText(size=(20, 1), default_text=path, k="AddrInput"),
                    sg.Text("Enter the directory path"),
                ],
                [
                    sg.Combo(comboList, k="FunctionInput"),
                    sg.Text("Choose the function"),
                ],
                [sg.Button("Next Step")],
            ]
            window1 = sg.Window("main", layout1).Finalize()
            firstWindow(True, window1)


def ErrorWindow(run, window):
    while run:
        event, values = window.read()
        if event in ("Close Window"):
            run = False


run = True

firstWindow(run, window1)
