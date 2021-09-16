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
#layout = [[]]

# CREATE A WINDOW THAT WILL STAY OPEN AND OFFER OPTIONS OF WHICH TDA DATA TO GET 

#window = sg.Window(title="FinData", layout=layout, margins=(400, 275)) # add .read() to outside variable

# CREATING AN EVENT LOOP FOR WHEN SOMETHING IS PRESSED AND RETURNING THE REQUIRED RESULTS
"""
while True:
    event, values = window.read()
    #End program if user closes window
    # or if OK is pressed (this will be changed)
    if event == "OK" or event == sg.WIN_CLOSED: 
        break
window.close()
"""

""" Create a Image viewer that I will turn into a python script viewer that will 
let me run any script I create from this window"""

file_list_column = [
    [
        sg.Text("Image Viewer/File Viewer"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    # Creating a browse button that I will use to find folders with images in it
    # The key param is important!!! This is used to identify a specific element 
    # Which will then be used to access the contents of the element
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")
        # The Listbox() element will display a list of paths to the images that you can choose from
        # you can prefill this by passing in a list of strings. 
        # When first loading, you want this to be empty. So pass EMPTY list then turn on events 
    ],
]

# CREATE THE RIGHT HAND COLUMN 
image_viewer_column = [
    [sg.Text("Choose an image from the list on the left: ")],
    [sg.Text(size=(40,1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")], # The image element has a key so you can refer back to this element later
]

# CREATE THE LAYOUT OF OUR FILE VIEWER
layout = [
    [
        # Notice how this list controls how the columns are set up in the program. 
        # VSeperator is an alias for Vertical Seperator() to learn more about the 
        # Column() and VerticalSeperator() read their documentation. 
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)

# NOW CREATE THE WHILE LOOP THAT WILL KEEP THE PROGRAM RUNNING. 
while True:
    # remember this infinite loop controls the logic of the GUI. The {event} will contain the 
    # "key" string of which ever element the user interacts with. The {values} variable will 
    # contain a Python Dictionary that maps the element key to a value. 
    # EXAMPLE: IF user picks a folder, THEN -FOLDER- will map to the folder path! 
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break


# THE FOLDER NAME WAS FILLED IN, NOW MAKE A LIST OF FILES IN THE FOLDER
# This will be the programs conditional statements. This will contain all the conditions that 
# the user will be allowed to "use" or access. This sets the "rules" for the UI
if event == "-FOLDER-":
    folder = values["-FOLDER-"]
    try: 
        # Get the list of files in folder 
        file_list = os.listdir(folder)
    except: 
        file_list = []

    fnames = [
        f 
        for f in file_list
        if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith((".png", ".gif"))
    ]
# In the above event I am checking the event against the "-FOLDER-" key created earlier. 
# which refers to the In() element. So if the event "exists" then the user has chosen an 
# element in the UI so then I use the os.listdir() method to get the file listings.
# after that, I filtered down the files that are displayed to only the .png and .gif
    window["-FILE LIST-"].update(fnames)

# NOW I NEED TO CREATE THE ELIF STATEMENT 
elif event == "-FILE LIST-": # meaning a file was chosen fromt the listbox()
    try:
        filename = os.path.join(
            values["-FOLDER-"], values["-FILE LIST-"][0]
            )
        window["-TOUT-"].update(filename)
        window["-IMAGE-"].update(filename=filename)
    except:
        pass

# FINALLY WE NOW NEED TO END THE PROGRAM: 
window.close() # simple enough! 























