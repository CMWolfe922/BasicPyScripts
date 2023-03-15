#!/usr/bin/env python3

from tkinter import *
import sqlite3 as db

# TODO: FUNCTION TO CONNECT TO DATABASE AND SAVE
conn = db.connect('Users.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS USERS
    (
        Fname TEXT,
        Lname TEXT,
        email TEXT,
        password TEXT
    )""")

cur.close()
conn.commit()
conn.close()

# TODO: CREATE METHOD FOR PUTTING DATA IN DATABASE
def put():
    conn = db.connect('Users.db')
    cur = conn.cursor()
    cur.execute("insert into Users values('%s', '%s', '%s', '%s')"%(fname.get(), lname.get(), user_email.get(), password.get()))
    cur.close()
    conn.commit()
    conn.close()
    status.set('Data Added Successfully!')


# creating the GUI:
master = Tk()

# TODO: CREATE VARIABLES FOR ACCESSING ENTRY BOX LABELS:
fname = StringVar()
lname = StringVar()
user_email = StringVar()
password = StringVar()
status = StringVar()

# creating labels for instructing the user on what to do
# use grid layout for better GUI layout control
Label(master, text='First Name: ').grid(row=0, column=0)
    
Label(master, text='Email Address: ').grid(row=2, column=0)
Label(master, text='Password: ').grid(row=2, column=1)
Label(master, text='', textvariable=status).grid(row=4, columnspan=2)

# creating entry boxes for taking inputs:
Entry(master, textvariable=fname).grid(row=1, column=0)
Entry(master, textvariable=lname).grid(row=1, column=1)
Entry(master, textvariable=user_email).grid(row=3, column=0)
Entry(master, textvariable=password).grid(row=3, column=1)

# adding button for submitting data:
# columnspan decides how much column space is to be given
# command specifies button action
Button(master, text='Submit', command=put()).grid(row=5, columnspan=2)

mainloop()
