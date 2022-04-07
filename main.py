import PySimpleGUI as sg

# #NON-PERSISTENT WINDOW
# layout = [[sg.Text('My one-shot window.')], [sg.InputText()],
#           [sg.Submit(), sg.Cancel()]]

# window = sg.Window('Window Title', layout)

# event, values = window.read()
# window.close()

# text_input = values[0]
# sg.popup('You entered', text_input)

# ##
# event, values = sg.Window(
#     'Login Window',
#     [[sg.T('Enter your Login ID'),
#       sg.In(key='-ID-')], [sg.B('OK'), sg.B('Cancel')]]).read(close=True)

# login_id = values['-ID-']

# ## PERSISTENT WINDOW
# sg.theme('DarkAmber')  # Keep things interesting for your users

# layout = [[sg.Text('Persistent window')], [sg.Input(key='-IN-')],
#           [sg.Button('Read'), sg.Exit()]]

# window = sg.Window('Window that stays open', layout)

# while True:  # The Event Loop
#     event, values = window.read()
#     print(event, values)
#     if event == sg.WIN_CLOSED or event == 'Exit':
#         break

# window.close()

##
sg.theme('BluePurple')

layout = [[
    sg.Text('Your typed chars appear here:'),
    sg.Text(size=(15, 1), key='-OUTPUT-')
], [sg.Input(key='-IN-')], [sg.Button('Show'),
                            sg.Button('Exit')]]

window = sg.Window('Pattern 2B', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()