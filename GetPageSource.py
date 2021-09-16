#!usr/bin/env python3

import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
import requests
import re

# VARIABLES THAT STORE WEBSITES AND WEBSITE PAGES TEXT FILES
cnbc = "cnbc-urls.txt"

# READ ALL THE URL LINKS IN THE .TXT FILE
def read_txt(file, *args):

    with open(file, 'r') as pages:
        return pages.read()
        pages.close()

tfile = read_txt(cnbc)


# GET THE HTML FROM A WEBPAGE
def get_urls(tfile, *args):

    with open(tfile,'r') as f:
        for line in f:
            #do not forget to strip the trailing new line
            urls = line.rstrip("\n")
            return urls

address = get_urls(cnbc)

print(address)