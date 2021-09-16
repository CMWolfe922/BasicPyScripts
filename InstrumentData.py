#!usr/bin/env python3
"""
THIS SCRIPT IS THE GRAPHIC USER INTERFACE FOR GETTING THE
INSTRUMENT DATA FROM TD AMERITRADE. AS OF
NOW EACH FUNCTION WILL BE A SEPERATE POPUP WINDOW.

EVENTUALLY I WANT IT TO ALL BE ON ONE GUI WINDOW SO THAT
ALL THE PARAMETERS CAN BE PICKED AT THE SAME TIME.
"""
import PySimpleGUI as sg
import os.path

# CREATE THE DESIRED LAYOUT FOR THE MAIN WINDOW
"""
when creating a layout, remember that pysimplegui takes in nested lists to layout the 
display buttons and widgets. So each list inside the first list is a row. 
layout = [[Row 1], # these can take in text input, button, radio buttons and many more params.
		  [Row 2],
		  [Row 3]]
"""


# THIS WILL BE THE FIRST POP UP WINDDOW THAT POPS UP WHEN SOMEONE CHOOSES INSTRUMENT DATA
def ask_for_projection():
    """
    Determine what the projection type will be for instrument data 
    """
    projections = ['symbol-search', 'symbol-regex', 'desc-search', 'desc-regex', 'fundamental']

    sg.theme("darkamber") # change the theme in the universal file

    layout = [
        [sg.Text('What search projection would you like to use?')],
        [sg.Button(button_text='symbol-search', enable_events=True),
         sg.Button(button_text='symbol-regex', enable_events=True),
         sg.Button(button_text='desc-search', enable_events=True),
         sg.Button(button_text='desc-regex', enable_events=True),
         sg.Button(button_text='fundamental', enable_events=True)],
    ]

    window = sg.Window('Pick Instrument Data Projection Format: ', layout)
    event, values = window.read()
    window.close()

    if event == 'symbol-search':
        return projections[0]
    if event == 'symbol-regex':
        return projections[1]
    if event == 'desc-search':
        return projections[2]
    if event == 'desc-regex':
        return projections[3]
    elif event == 'fundamental':
        return projections[4]