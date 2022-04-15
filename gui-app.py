#!/usr/bin/env python3

import PySimpleGUI as sg
from temperature_measure import *


def make_window(theme):
    sg.theme(theme)
    menu_def = [['&Application', ['&Exit']], ['&Help', ['&About']]]

    app_layout = [[
        sg.B('Air temperature', size=(20, 1)),
        sg.ProgressBar(100,
                       orientation='h',
                       size=(20, 20),
                       key='-PROGRESS BAR AIR-'),
        sg.Text(size=(5, 1), key='-AIR DISPLAY-'),
        sg.Text("°C")
    ],
    [
        sg.B('Canopy temperature', size=(20, 1)),
        sg.ProgressBar(100,
                        orientation='h',
                        size=(20, 20),
                        key='-PROGRESS BAR CANOPY-'),
        sg.Text(size=(5, 1), key='-CANOPY DISPLAY-'),
        sg.Text("°C")
    ],
    [
        sg.B('Dew temperature', size=(20, 1)),
        sg.ProgressBar(100,
                        orientation='h',
                        size=(20, 20),
                        key='-PROGRESS BAR DEW-'),
        sg.Text(size=(5, 1), key='-DEW DISPLAY-'),
        sg.Text("°C")
    ],
    [
        sg.B('Wnd speed', size=(20, 1)),
        sg.ProgressBar(100,
                        orientation='h',
                        size=(20, 20),
                        key='-PROGRESS BAR WIND-'),
        sg.Text(size=(5, 1), key='-WIND DISPLAY-'),
        sg.Text("m/s")
    ],
    [
        sg.B('Pressure', size=(20, 1)),
        sg.ProgressBar(100,
                        orientation='h',
                        size=(20, 20),
                        key='-PROGRESS BAR PRESSURE-'),
        sg.Text(size=(5, 1), key='-PRESSURE DISPLAY-'),
        sg.Text("hPa")
    ],
    [
        sg.B('Solar radiation', size=(20, 1)),
        sg.ProgressBar(100,
                        orientation='h',
                        size=(20, 20),
                        key='-PROGRESS BAR RADIATION-'),
        sg.Text(size=(5, 1), key='-RADIATION DISPLAY-'),
        sg.Text("Watt / s")
    ]]

    logging_layout = [
        [sg.Text("Anything printed will display here!")],
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
        ]
        # [sg.Output(size=(60,15), font='Courier 8', expand_x=True, expand_y=True)]
    ]

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
    window = sg.Window('Data collection application',
                       layout,
                       grab_anywhere=True,
                       resizable=True,
                       margins=(0, 0),
                       use_custom_titlebar=True,
                       finalize=True,
                       keep_on_top=True,
                       scaling=2.0)
    window.set_min_size(window.size)
    return window


def main():
    window = make_window(sg.theme())

    # This is the Event Loop
    ########################USE THREADS FOR LONG MEASUREMENTS (?)
    while True:
        event, values = window.read(timeout=100)
        # keep an animation running as to show that things are happening
        # window['-GIF-IMAGE-'].update_animation(sg.DEFAULT_BASE64_LOADING_GIF, time_between_frames=100)
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            print('============ Event = ', event, ' ==============')
            print('-------- Values Dictionary (key=value) --------')
            for key in values:
                print(key, ' = ', values[key])
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break

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


        elif event == "-GRAPH-":
            graph = window['-GRAPH-']  # type: sg.Graph
            graph.draw_circle(values['-GRAPH-'],
                              fill_color='yellow',
                              radius=20)
            print("[LOG] Circle drawn at: " + str(values['-GRAPH-']))
        elif event == "Set Theme":
            print("[LOG] Clicked Set Theme!")
            theme_chosen = values['-THEME LISTBOX-'][0]
            print("[LOG] User Chose Theme: " + str(theme_chosen))
            window.close()
            window = make_window(theme_chosen)
        elif event == 'Versions':
            sg.popup(sg.get_versions(), keep_on_top=True)
        elif event == 'About':
            print("[LOG] Clicked About!")
            sg.popup(
                'PySimpleGUI Demo All Elements',
                'Right click anywhere to see right click menu',
                'Visit each of the tabs to see available elements',
                'Output of event and values can be see in Output tab',
                'The event and values dictionary is printed after every event',
                keep_on_top=True)

    window.close()
    exit(0)


if __name__ == '__main__':
    # sg.theme('black')
    # sg.theme('dark red')
    sg.theme('dark green 7')
    # sg.theme('DefaultNoMoreNagging')
    main()
