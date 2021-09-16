#!usr/bin/env Python3

from urllib.request import urlopen
import re 


url = "https://www.cnbc.com/cryptocurrency/"

#SIMPLE SCRAPER v-0.2
# REGEX WAS ADDED TO THIS ONE

# use re.findall() to find any text within a string matching the regex 
# element. The * sign stands for 0 or more of whatever comes just before 
# the asterick. So the first argument re.findall("ab*C", "ac") is the rgular 
# expression that I want to match and the second argument is the string 
# to test. 
# So basically "find" ab*c in the string "ac" but the second argument doesn't
# have to be just a raw string. it can be a variable that calls on a 
# raw string. 
# re.findall("ab*c", "ac")
# The output would be: ['ac'] because the regex pattern will look for any 
# string that starts with 'a' and ends with 'c', AND has ZERO or MORE instances
# of 'b' between the two.  

page = urlopen(url)

html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

"""
1.) <title.*?> matches the opening <TITLE > tag in html. 
The <title part of the pattern matches with <TITLE because 
re.search() is called with re.IGNORECASE, and .*?> matches 
any text after <TITLE up to the first instance of >

2.) .*? non-greedily matches all text after the opening 
<TITLE >, stopping at the first match for </title.*?>.

3.) </title.*?> differs from the first pattern only in 
its use of the / character, so it matches the closing </title / > tag in html.
"""

print(title)

# create a regex that returns everything that comes after '>' and before '<'
# this will give me all the strings in an html file. To do this I need to use the
# '.' and the '*' together. The . says to find any single character in a regular expression

# This was the first attempt. Doesn't work with a findall() function. Try search()
# cleaned = re.findall("<.*>.*<.*>", html)
