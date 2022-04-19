#!/usr/bin/env python3

import PySimpleGUI as sg
from temperature_measure import *

class WindowOpenFile():
    def __init__(self, theme='BluePurple'):
        sg.theme(theme)
        
        layout = [
            [
                sg.Text('Type the path where you want your csv file to be saved:'),
            ],
            [
                sg.Input(size=(70, 1), key='-PATH-', default_text='/home/$USER/Documents/Vineyards_data/')
            ],
            [
                sg.Text('Type the name for your csv file:'),
            ],
            [
                sg.Input(size=(70, 1), key='-NAME-', default_text='')
            ],
            [
                sg.Button('Done'),
                sg.Button('Cancel')
            ]]

        window = sg.Window('Pattern 2B', layout)

        while True:
            event, values = window.read()
            print(event, values)
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            if event == 'Save':
                sg.Output()
                f = open()
                pass

        window.close()

def main():
    w = WindowOpenFile()
    

if __name__ == '__main__':
    main()