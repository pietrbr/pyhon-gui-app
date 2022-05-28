#!/usr/bin/env python3

import PySimpleGUI as sg
from csv import DictWriter
from Sensors.Camera import MLX90614_GY906
from Sensors.LightSensor import TSL2591
from Sensors.Pressure import BME280
from Sensors.Temperature import DHT22
from Sensors.UVSensor import LTR390

from random import random  # TODO: to be deleted

from FileManager.Openfile import WindowOpenFile


def make_window(theme):
    sg.theme(theme)
    menu_def = [['&Application', ['&Create and open file']],
                ['&Help', ['&About']]]

    app_layout = [
        [
            sg.Text('Location:', size=(10, 1)),
            sg.Input(size=(15, 1), key='-LOCATION-'),
            sg.Text('', size=(12, 1)),
            sg.Button('Save', size=(10, 1))
            # sg.Text('Lat:', size=(5, 1)),
            # sg.Text(size=(10, 1), key='-LAT DISPLAY-'),
            # sg.Text('Lon:', size=(5, 1)),
            # sg.Text(size=(10, 1), key='-LON DISPLAY-')
        ],
        [
            sg.Text('Wind speed:', size=(10, 1)),
            sg.Input(size=(15, 1), key='-WIND_SPEED-'),
            sg.Text("m/s")
        ],
        [
            sg.Button('Air temperature', size=(20, 1)),
            sg.ProgressBar(100,
                           orientation='h',
                           size=(10, 20),
                           key='-PROGRESS BAR AIR-'),
            sg.Text(size=(5, 1), key='-AIR DISPLAY-'),
            sg.Text("°C")
        ],
        [
            sg.Button('Canopy temperature', size=(20, 1)),
            sg.ProgressBar(100,
                           orientation='h',
                           size=(10, 20),
                           key='-PROGRESS BAR CANOPY-'),
            sg.Text(size=(5, 1), key='-CANOPY DISPLAY-'),
            sg.Text("°C")
        ],
        [
            sg.Button('Humidity', size=(20, 1)),
            sg.ProgressBar(100,
                           orientation='h',
                           size=(10, 20),
                           key='-PROGRESS BAR HUMIDITY-'),
            sg.Text(size=(5, 1), key='-HUMIDITY DISPLAY-'),
            sg.Text("%")
        ],
        [
            sg.Button('Pressure', size=(20, 1)),
            sg.ProgressBar(100,
                           orientation='h',
                           size=(10, 20),
                           key='-PROGRESS BAR PRESSURE-'),
            sg.Text(size=(5, 1), key='-PRESSURE DISPLAY-'),
            sg.Text("hPa")
        ],
        [
            sg.Button('Solar radiation', size=(20, 1)),
            sg.ProgressBar(100,
                           orientation='h',
                           size=(10, 20),
                           key='-PROGRESS BAR RADIATION-'),
            sg.Text(size=(5, 1), key='-RADIATION DISPLAY-'),
            sg.Text("W/m\u00b2")
        ]
    ]

    logging_layout = [[sg.Text("Anything printed will display here!")],
                      [
                          sg.Multiline(size=(60, 15),
                                       font='Courier 8',
                                       expand_x=True,
                                       expand_y=True,
                                       write_only=True,
                                       reroute_stdout=True,
                                       reroute_stderr=True,
                                       echo_stdout_stderr=True,
                                       autoscroll=True,
                                       auto_refresh=True)
                      ]]

    theme_layout = [[
        sg.Text(
            "See how elements look under different themes by choosing a different theme here!"
        )
    ],
                    [
                        sg.Listbox(values=sg.theme_list(),
                                   size=(20, 12),
                                   key='-THEME LISTBOX-',
                                   enable_events=True)
                    ], [sg.Button("Set Theme")]]

    layout = [[
        sg.MenubarCustom(menu_def,
                         key='-MENU-',
                         font='Courier 15',
                         tearoff=False)
    ]]
    layout += [[
        sg.TabGroup([[
            sg.Tab('Measures', app_layout),
            sg.Tab('Logs', logging_layout),
            sg.Tab('Themes', theme_layout)
        ]],
                    key='-TAB GROUP-',
                    expand_x=True,
                    expand_y=True),
    ]]
    layout[-1].append(sg.Sizegrip())
    window = sg.Window(
        'Data collection application',
        layout,
        grab_anywhere=True,
        resizable=True,
        margins=(0, 0),
        # use_custom_titlebar=True,
        finalize=True,
        keep_on_top=True,
        scaling=1.0)
    window.set_min_size(window.size)
    return window


def main():
    window = make_window(sg.theme())
    fpath = None
    # headers for csv file
    headersCSV = [
        'CODE', 'LAT', 'LON', 'AIR_TEMP', 'CANOPY_TEMP', 'HUM', 'WIND_SPEED',
        'PRESSURE', 'SOLAR_RAD'
    ]
    # keys of dictonary for displayed values
    display_dict = [
        # '-LAT DISPLAY-', '-LON DISPLAY-',
        '-AIR DISPLAY-',
        '-CANOPY DISPLAY-',
        '-HUMIDITY DISPLAY-',
        '-PRESSURE DISPLAY-',
        '-RADIATION DISPLAY-'
    ]
    # keys of dictonary for displayed bars
    bar_dict = [
        '-PROGRESS BAR AIR-', '-PROGRESS BAR CANOPY-',
        '-PROGRESS BAR HUMIDITY-', '-PROGRESS BAR PRESSURE-',
        '-PROGRESS BAR RADIATION-'
    ]
    # dictonary for values acquired
    # reset dictonary values to 'None' to get ready for next collection
    dict = {
        'CODE': None,
        'LAT': None,
        'LON': None,
        'AIR_TEMP': None,
        'CANOPY_TEMP': None,
        'HUM': None,
        'WIND_SPEED': None,
        'PRESSURE': None,
        'SOLAR_RAD': None
    }
    value = None
    window['-LOCATION-'].update('')  # CODE
    for key in display_dict:  # -DISPLAY-
        window[key].update('-')
    for key in bar_dict:  # -PROGRESS BAR-
        window[key].update(0)

    # ---------------------------------------------------
    # Initialize Each Sensor
    # ---------------------------------------------------
    tempSensor  = DHT22('Sensore di Temperatura e Umidità')
    lightSensor = TSL2591('Sensore di Luce Ambientale')
    uvSensor    = LTR390('Sensore Radiazione Ultravioletta')
    cameraIR    = MLX90614_GY906('Sensore di Temperatura Superficiale')
    pressSensor = BME280('Sensore di Pressione, Temperatura e umidità')
    
    pressSensor.get_calib_param()
    # ---------------------------------------------------

    while True:  # This is the Event Loop
        event, values = window.read(timeout=100)
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            print('=======================================\n', 'EVENT = ',
                  event)
            le = 0
            for key in values:
                if len(key) > le:
                    le = len(key)
            for key in values:
                print(' ' * 6, key, ' ' * (le - len(key)), '= ', values[key])
        if event in (None, 'Exit'):
            print("EVENT = Clicked Exit!")
            break

        ### SENSOR ACQUISITION ###
        elif event == 'Air temperature':
            value, _    = tempSensor.measure()
            # _, temp, _  = pressSensor.measure()
            # value = (value + temp)/2 # Take the average between the two temp by diff sensors
            window['-AIR DISPLAY-'].update("{:.2f}".format(
                value))  # TODO: change here for acquisition # DONE
            progress_bar = window['-PROGRESS BAR AIR-']
            [progress_bar.update(current_count=i + 1) for i in range(100)]
            dict['AIR_TEMP'] = round(value, 2)
            value = None
            print("[LOG] Air temperature measurement complete!")

        elif event == 'Canopy temperature':
            value =  cameraIR.measure() # TODO: change here for acquisition
            window['-CANOPY DISPLAY-'].update("{:.2f}".format(value))
            progress_bar = window['-PROGRESS BAR CANOPY-']
            [progress_bar.update(current_count=i + 1) for i in range(100)]
            dict['CANOPY_TEMP'] = round(value, 2)
            value = None
            print("[LOG] Canopy temperature measurement complete!")

        elif event == 'Humidity':
            _, value = tempSensor.measure()
            # _, _, temp  = pressSensor.measure()
            # value = (value + temp)/2
            window['-HUMIDITY DISPLAY-'].update("{:.2f}".format(
                value))  # TODO: change here for acquisition # DONE
            progress_bar = window['-PROGRESS BAR HUMIDITY-']
            [progress_bar.update(current_count=i + 1) for i in range(100)]
            dict['HUM'] = round(value, 2)
            value = None
            print("[LOG] Humidity measurement complete!")

        elif event == 'Pressure':
            value = pressSensor.measure()  # TODO: change here for acquisition
            window['-PRESSURE DISPLAY-'].update("{:.2f}".format(value))
            progress_bar = window['-PROGRESS BAR PRESSURE-']
            [progress_bar.update(current_count=i + 1) for i in range(100)]
            dict['PRESSURE'] = round(value, 2)
            value = None
            print("[LOG] Pressure measurement complete!")

        elif event == 'Solar radiation':
            temp = lightSensor.measure()
            value = uvSensor.measure()
            value = value + temp
            window['-RADIATION DISPLAY-'].update(
                "{:.2f}".format(value))  # TODO: change here for acquisition
            progress_bar = window['-PROGRESS BAR RADIATION-']
            [progress_bar.update(current_count=i + 1) for i in range(100)]
            dict['SOLAR_RAD'] = round(value, 2)
            value = None
            print("[LOG] Solar radiation measurement complete!")

        elif event == "Set Theme":
            print("[LOG] Clicked Set Theme!")
            theme_chosen = values['-THEME LISTBOX-'][0]
            print("[LOG] User Chose Theme: " + str(theme_chosen))
            window.close()
            window = make_window(theme_chosen)

        ### CREATE AND OPEN FILE ###
        elif event == 'Create and open file':
            print('[LOG] Clicked Create and open file')
            window_open_file = WindowOpenFile(headersCSV, theme=sg.theme())
            fpath = window_open_file.getfilename(
            )[:]  # attach [:] to make a copy of the string
            print('[LOG] File created and saved; path: ', fpath)
            del window_open_file

        ### SAVE DATA TO FILE ###
        # check here on how to write csv files: https://www.delftstack.com/howto/python/python-append-to-csv/
        elif event == 'Save':
            print('[LOG] Clicked Save!')
            with open(fpath, 'a', newline='') as f:
                dict['CODE'] = values['-LOCATION-']
                dict['WIND_SPEED'] = values['-WIND_SPEED-']
                dict['LAT'] = random(
                )  # TODO: use module for GPS, delete random()
                dict['LON'] = random(
                )  # TODO: use module for GPS, delete random()
                dictwriter = DictWriter(f, fieldnames=headersCSV)
                dictwriter.writerow(dict)
                f.close()
            # reset dict entries and values to 'None' to get ready for next collection
            dict = {
                'CODE': None,
                'LAT': None,
                'LON': None,
                'AIR_TEMP': None,
                'CANOPY_TEMP': None,
                'HUM': None,
                'WIND_SPEED': None,
                'PRESSURE': None,
                'SOLAR_RAD': None
            }
            value = None
            for key in display_dict:
                window[key].update('-')
            for key in bar_dict:
                window[key].update(0)
            for key in ['-LOCATION-', '-WIND_SPEED-']:
                window[key].update('')

        elif event == 'About':
            print("[LOG] Clicked About!")
            sg.popup(
                'Application for the collection of data for the ANSIA Team of the ASP Program XVIII cycle.',
                'The application was kindly designed by the online boys.',
                'The application is based on the design provided in the PySimpleGUI Demo All Elements.',
                '',
                # 'The app may contain an easter egg...',
                '',
                keep_on_top=True)

    window.close()
    exit(0)


if __name__ == '__main__':
    sg.theme('Python')
    main()
