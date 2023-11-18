import PySimpleGUI as sg

sg.theme('DarkBlue12')
layout = [  [sg.Combo(['irrelevantWords', 'importantWords', 'mostUsedWords', 'whoTalkAbout', 'firstToSay', 'universalWords']), sg.Text("Choose the function")],
            [sg.InputText(size=(20, 1)), sg.Text("Enter the arguments")],
            [sg.Push(), sg.Output(size=(40, 20))],
            [sg.Button('Launch'), sg.Push(), sg.Button('Close Window')]
        ]

window = sg.Window('Test', layout).Finalize()

while True:
    event, values = window.read()
    if event in (None, 'Close Window'):
        break

window.close()