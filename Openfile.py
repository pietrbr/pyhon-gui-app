#!/usr/bin/env python3

import PySimpleGUI as sg
import os

class WindowOpenFile():
    def __init__(self, theme='BluePurple'):
        self.path = '/home/$USER/Documents/Vineyards_data/'
        self.name = 'data1'
        self.file = None
        
        sg.theme(theme)
        layout = [
            [
                sg.Text('Type the path where you want your csv file to be saved:'),
            ],
            [
                sg.Input(size=(70, 1), key='-PATH-', default_text='/home/ppp/Documents/Vineyards_data/')
            ],
            [
                sg.Text('Type the name for your csv file:'),
            ],
            [
                sg.Input(size=(70, 1), key='-NAME-', default_text='')
            ],
            [
                sg.Button('Open'),
                sg.Button('Cancel')
            ]]

        window = sg.Window('Open file', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            if event == 'Open':
                self.path = values['-PATH-']
                self.name = values['-NAME-']
                try:
                    os.mkdir(self.path)
                self.file = open(self.path+self.name+'.csv', 'w+')
                pass

        window.close()

def main():
    w = WindowOpenFile()
    print(w.file)

if __name__ == '__main__':
    main()