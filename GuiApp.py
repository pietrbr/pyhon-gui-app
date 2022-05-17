#!/usr/bin/env python3

# TODO: canopy temeprature si raccoglie attraverso la camera termica
# TODO: aggiungere tab per la raccolta foto

from turtle import window_width

import PySimpleGUI as sg

from slave_module import *

from Openfile import WindowOpenFile
from SaveFile import WindowSaveFile


def make_window(theme):
    sg.theme(theme)
    menu_def = [['&Application', ['&Create and open file (csv)', '&Save file (tiff)']],
                ['&Help', ['&About']]]

    app_layout = [[
        sg.Text('Location:', size=(10, 1)),
        sg.Input(size=(30, 1), key='-LOCATION-')
    ],
                  [
                      sg.Button('Air temperature', size=(20, 1)),
                      sg.ProgressBar(100,
                                     orientation='h',
                                     size=(20, 20),
                                     key='-PROGRESS BAR AIR-'),
                      sg.Text(size=(5, 1), key='-AIR DISPLAY-'),
                      sg.Text("°C")
                  ],
                  [
                      sg.Button('Canopy temperature', size=(20, 1)),
                      sg.ProgressBar(100,
                                     orientation='h',
                                     size=(20, 20),
                                     key='-PROGRESS BAR CANOPY-'),
                      sg.Text(size=(5, 1), key='-CANOPY DISPLAY-'),
                      sg.Text("°C")
                  ],
                  [
                      sg.Button('Dew temperature', size=(20, 1)),
                      sg.ProgressBar(100,
                                     orientation='h',
                                     size=(20, 20),
                                     key='-PROGRESS BAR DEW-'),
                      sg.Text(size=(5, 1), key='-DEW DISPLAY-'),
                      sg.Text("°C")
                  ],
                  [
                      sg.Button('Wind speed', size=(20, 1)),
                      sg.ProgressBar(100,
                                     orientation='h',
                                     size=(20, 20),
                                     key='-PROGRESS BAR WIND-'),
                      sg.Text(size=(5, 1), key='-WIND DISPLAY-'),
                      sg.Text("m/s")
                  ],
                  [
                      sg.Button('Pressure', size=(20, 1)),
                      sg.ProgressBar(100,
                                     orientation='h',
                                     size=(20, 20),
                                     key='-PROGRESS BAR PRESSURE-'),
                      sg.Text(size=(5, 1), key='-PRESSURE DISPLAY-'),
                      sg.Text("hPa")
                  ],
                  [
                      sg.Button('Solar radiation', size=(20, 1)),
                      sg.ProgressBar(100,
                                     orientation='h',
                                     size=(20, 20),
                                     key='-PROGRESS BAR RADIATION-'),
                      sg.Text(size=(5, 1), key='-RADIATION DISPLAY-'),
                      sg.Text("W/m\u00b2")
                  ], [sg.Button('Save', size=(10, 3))]]

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

    graphing_layout = [[
        sg.Text("Anything you would use to graph will display here!")
    ],
                       [
                           sg.Graph((200, 200), (0, 0), (200, 200),
                                    background_color="black",
                                    key='-GRAPH-',
                                    enable_events=True)
                       ], [sg.T('Click anywhere on graph to draw a circle')]]

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
            sg.Tab('Graphs', graphing_layout),
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
        scaling=4.0)
    window.set_min_size(window.size)
    return window


def main():
    window = make_window(sg.theme())

    ### USE THREADS FOR LONG-LASTING MEASUREMENTS
    while True:  # This is the Event Loop
        event, values = window.read(timeout=100)
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            print('============ Event = ', event, ' ==============')
            print('-------- Values Dictionary (key=value) --------')
            for key in values:
                print(key, ' = ', values[key])
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break

        ### SENSOR ACQUISITION ###
        elif event == 'Air temperature':
            meas = TemperatureMeasure()
            window['-AIR DISPLAY-'].update("{:.2f}".format(
                meas.measure_avg_3()))
            progress_bar = window['-PROGRESS BAR AIR-']
            [progress_bar.update(current_count=i + 1) for i in range(100)]
            print("[LOG] Temperature measurement complete!")

        elif event == 'Canopy temperature':
            meas = TemperatureMeasure()
            window['-CANOPY DISPLAY-'].update("{:.2f}".format(
                meas.measure_avg_3()))
            progress_bar = window['-PROGRESS BAR CANOPY-']
            [progress_bar.update(current_count=i + 1) for i in range(100)]
            print("[LOG] Temperature measurement complete!")

        elif event == 'Dew temperature':
            meas = TemperatureMeasure()
            window['-DEW DISPLAY-'].update("{:.2f}".format(
                meas.measure_avg_3()))
            progress_bar = window['-PROGRESS BAR DEW-']
            [progress_bar.update(current_count=i + 1) for i in range(100)]
            print("[LOG] Temperature measurement complete!")

        elif event == 'Wind speed':
            meas = TemperatureMeasure()
            window['-WIND DISPLAY-'].update("{:.2f}".format(
                meas.measure_avg_3()))
            progress_bar = window['-PROGRESS BAR WIND-']
            [progress_bar.update(current_count=i + 1) for i in range(100)]
            print("[LOG] Temperature measurement complete!")

        elif event == 'Pressure':
            meas = TemperatureMeasure()
            window['-PRESSURE DISPLAY-'].update("{:.2f}".format(
                meas.measure_avg_3()))
            progress_bar = window['-PROGRESS BAR PRESSURE-']
            [progress_bar.update(current_count=i + 1) for i in range(100)]
            print("[LOG] Temperature measurement complete!")

        elif event == 'Solar radiation':
            meas = TemperatureMeasure()
            window['-RADIATION DISPLAY-'].update("{:.2f}".format(
                meas.measure_avg_3()))
            progress_bar = window['-PROGRESS BAR RADIATION-']
            [progress_bar.update(current_count=i + 1) for i in range(100)]
            print("[LOG] Temperature measurement complete!")

        # elif event == "-GRAPH-":
        #     graph = window['-GRAPH-']  # type: sg.Graph
        #     graph.draw_circle(values['-GRAPH-'],
        #                       fill_color='yellow',
        #                       radius=20)
        #     print("[LOG] Circle drawn at: " + str(values['-GRAPH-']))

        elif event == "Set Theme":
            print("[LOG] Clicked Set Theme!")
            theme_chosen = values['-THEME LISTBOX-'][0]
            print("[LOG] User Chose Theme: " + str(theme_chosen))
            window.close()
            window = make_window(theme_chosen)

        ### CREATE AND OPEN FILE ###
        elif event == 'Create and open file':
            print('[LOG] Clicked Create and open file')
            window_open_file = WindowOpenFile()
            fp = window_open_file.getfpointer()

        elif event == 'Save file':
            print('[LOG] Clicked Save file')
            

        elif event == 'About':
            print("[LOG] Clicked About!")
            sg.popup(
                'Application for the collection of data for the ANSIA Team of the ASP Program XVIII cycle.',
                'The application was kindly designed by the online boys.',
                'The application is based on the design provided in the PySimpleGUI Demo All Elements.',
                '',
                'The app may contain an easter egg...',
                '',
                keep_on_top=True)

    window.close()
    exit(0)


if __name__ == '__main__':
    # sg.theme('black')
    # sg.theme('dark red')
    sg.theme('dark green 7')
    sg.theme('BluePurple')
    sg.theme('Python')
    # sg.theme('DefaultNoMoreNagging')
    main()
