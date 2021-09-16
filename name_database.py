#!/usr/bin/env python3

"""
This script is for allowing the user to decide the name
of the database, as well as checking for whether or not
the user has already created a database.
"""
import PySimpleGUI as sg

# TODO: MAKE FUNCTION THAT BUILDS A GUI FOR USER INPUT
def name_database():
	"""
    :param: This function will take in no parameters. It 
    will only be for setting the name of the database. 

    :action: creates a GUI for the user to set the 
    name of the Database. There will be a try/except
    block to make sure that name has not already been 
    used.

    :returns: name of database file, and the path for 
    where the DB file is stored 
	"""
    name = []
    theme = sg.theme('darkamber')

    layout = [
        [sg.Text("Enter the name of your database: ")],
        [sg.Text('Databse Name: ', size=(15, 1)), sg.InputText()],
        [sg.Text('Path to Database: ', size=(300,1)), sg.InputText()]
        ]



# TODO: TRY/EXCEPT BLOCK CHECKING FOR EXISTING DB


# TODO: SET VARIABLE == TO GUI EVENT (DATABASE NAME)


# TODO: CREATE TRY/EXCEPT BLOCK FOR ERROR HANDLING