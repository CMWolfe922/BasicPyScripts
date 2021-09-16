#!usr/bin/env python3
"""
Creating a database for raw JSON data

"""
import sqlite3
from sqlite3 import Error

path = "C:/Users/thesi/PycharmProjects/TD-Ameritrade-API/databases"

# THIS FUNCTION CREATES A CONNECTION TO THE DATABASE. IF THERE IS NO 
# DATABASE AT THE LOCATION SPECIFIED IT WILL CREATE ONE. 

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# CREATE A TABLE TO STORE USER DATA IN THE CREATED DATABASE. 

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")