import PySimpleGUI as sg

sg.theme('DarkBlue12')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Combo(['irrelevantWords', 'importantWords', 'mostUsedWords', 'whoTalkAbout', 'firstToSay', 'universalWords']), sg.Text("Choose the function")],
            [sg.InputText(size=(20, 1)), sg.Text("Enter the arguments")],
            [sg.Push(), sg.Output(size=(40, 20))],
            [sg.Button('Launch'), sg.Push(), sg.Button('Close Window')]
        ]

# Create the Window
window = sg.Window('Test', layout).Finalize()
#window.Maximize()
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Close Window'): # if user closes window or clicks cancel
        break
    print('You entered in the textbox:')
    print(values['textbox'])  # get the content of multiline via its unique key

window.close()