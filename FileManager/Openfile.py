#!/usr/bin/env python3

import os
from csv import DictWriter, writer

import PySimpleGUI as sg


class WindowOpenFile():

    def __init__(self, headersCSV, theme='BluePurple'):
        # self.path = os.path.dirname(os.path.realpath(__file__)) + '/../DataCollected/'
        self.path = cwd = os.getcwd(
        ) + '/DataCollected/'  # for current working directory

        # default values
        self.name = 'data'  # file name
        self.type = '.csv'  # file type

        # window
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
                  ], [sg.Button('Open'),
                      sg.Button('Cancel')]]

        window = sg.Window('Open file',
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
                if os.path.exists(self.path + self.name + self.type):
                    window['-WARNING-'].update('FILE ALREADY EXISTS')
                else:
                    # create the directory in case it does not exists
                    try:
                        os.mkdir(self.path)
                    except:
                        pass
                    with open(self.path + self.name + self.type,
                              'w',
                              newline='') as f:
                        w = writer(f)
                        w.writerow(headersCSV)
                        f.close()
                    print('File name: ' + self.path + self.name + self.type)
                    window.close()

    def getfilename(self):
        return self.path + self.name + self.type


def main():
    dict = {
        'CODE': None,
        'LAT': None,
        'LON': None,
        'AIR TEMP': None,
        'CANOPY TEMP': None,
        'DEW TEMP': None,
        'WIND SPEED': None,
        'PRESSURE': None,
        'SOLAR RAD': None
    }
    w = WindowOpenFile()
    filename = w.getfilename()
    print(filename, type(filename))


if __name__ == '__main__':
    main()
