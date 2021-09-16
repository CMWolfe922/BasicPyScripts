#!usr/bin/env python3

"""
This script will be on taking in data that is 
formatted in a json dump format, and reshaping the 
data into a numpy array. From there I will test 
if using a numpy array is better than pandas DF
"""

import numpy as np
import re
import pandas as pd
import sqlite3 as sql
import json


f = "RawDataFromStream.json"

# LETS CREATE A WAY TO READ FROM A JSON FILE 

# FIXING JSON FILE FORMAT
def fix_json(file):

    with open(file, "r+") as read_file:
        data = read_file.read()
        x = re.sub("\w+\((.+)\)", r'\1', data)
        with open(x) as json_file:
            json.loads(x)
            return json_file

        #read_file.close()
        #return x

        
data = fix_json(f)
print(data)


def iter_data(data):
    _iter = json.load(data)
    return _iter


def extract_data(data):
    data_dict = {}

    for k,v in data:
        data_dict[k] = data.keys()
        data_dict[v] = data.values()
        return data_dict

clean = iter_data(data)
print(clean)