# ====================================================================== #
# ++++++++++++++|      Individual Stock Sentiment      |++++++++++++++++ #
# ====================================================================== #
""" This endpoint returns scraped sentiment data from various social 
medias and shows how much an individual stock is being talked discussed, as 
well as how positive or negative the chatter is. """

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------

import http.client

conn = http.client.HTTPSConnection("styvio-stock-market-data.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "styvio-stock-market-data.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/sentiment/AAPL", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------

import requests

url = "https://styvio-stock-market-data.p.rapidapi.com/sentiment/AAPL"

headers = {
    'x-rapidapi-host': "styvio-stock-market-data.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


# ====================================================================== #
# +++++++++++++++++|      individual stock data    |++++++++++++++++++++ #
# ====================================================================== #
"""
This endpoint returns price arrays, as well as news and fundamental 
information about any given stock ticker.
"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("styvio-stock-market-data.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "styvio-stock-market-data.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/AAPL", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://styvio-stock-market-data.p.rapidapi.com/AAPL"

headers = {
    'x-rapidapi-host': "styvio-stock-market-data.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)