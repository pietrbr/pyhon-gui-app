#!/usr/bin/env python3

import os

import PySimpleGUI as sg


class WindowSaveFile():

    def __init__(self, theme='BluePurple'):
        self.path = os.path.dirname(
            os.path.realpath(__file__)) + '/DataCollected/'
        # self.path = cwd = os.getcwd()  # for current working directory
        try:
            os.mkdir(self.path)
        except:
            pass
        self.name = 'data'
        self.fp = None

        sg.theme(theme)
        layout = [[
            sg.Text('Type the path where you want your file to be saved:'),
        ], [sg.Input(size=(70, 1), key='-PATH-', default_text=self.path)],
                  [
                      sg.Text('Type the name for your file:'),
                      sg.Text(size=(35, 1), key='-WARNING-')
                  ],
                  [
                      sg.Input(size=(70, 1),
                               key='-NAME-',
                               default_text=self.name)
                  ], [sg.Button('Save'),
                      sg.Button('Cancel')]]

        window = sg.Window('Save file',
                           layout,
                           finalize=True,
                           keep_on_top=True)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            if event == 'Open':
                self.path = values['-PATH-']
                self.name = values['-NAME-']
                if os.path.exists(self.path + self.name + '.tif'):
                    window['-WARNING-'].update('FILE ALREADY EXISTS')
                else:
                    self.fp = open(self.path + self.name + '.tif', 'w+')
                    print('File name: ' + self.path + self.name + '.tif')
                    window.close()

    def getfpath(self):
        return self.path + self.name + '.tif'


def main():
    w = WindowSaveFile()
    fp = w.getfpointer()
    print(fp, type(fp))


if __name__ == '__main__':
    main()
