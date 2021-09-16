#!usr/bin/env Python3
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup as bs
import re

#----------------paste this code into your program / script----------------#
# determine if a password matches the secret password by
# comparing SHA256 hash codes.

def PasswordMatches(password, hash):
    password_utf = password.encode('utf-8')
    sha256hash = hashlib.sha256()
    sha256hash.update(password_utf)
    password_hash = sha256hash.hexdigest()
    if password_hash == hash:
        return True
    else:
        return False

# this is where you copy and paste the hash generated by
# the gui window
login_password_hash = 'ac6bd1a2caf560356daef1f1de5fd97b8f464b3059f442904a19c92f8fd24282'
password = sg.popup_get_text('Password', password_char='*')

if PasswordMatches(password, login_password_hash):
    print('LOGIN SUCCESSFUL')
else:
    print('login FAILED!!')
#------------------------------------------------------------------------------------------#


#url = "https://www.cnbc.com/investing/"
url = "https://www.cnbc.com/2020/10/06/here-are-bank-of-americas-early-retail-picks-for-the-holiday-season.html"
# SIMPLE SCRAPER JUST TO GET THE HTML BACK. 
# SCRAPER 0.2 HAS REGEX IN IT. 

page = urlopen(url)

html = page.read().decode("utf-8")
soup = bs(html, features="html.parser")

pattern = "<a.*>.*</a>"

match_results = re.search(pattern, html, re.IGNORECASE)
links = match_results.group()
links = re.sub("<.*?>", "", links)

text = soup.get_text()
#print(text)
print(links)