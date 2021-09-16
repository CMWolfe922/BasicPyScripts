# Yahoo Finance APIs: These are APIs that extract data from yahoo. 

# I will include 2 examples for each API one will be the API
# using http.client and the other using the API with requests

# ====================================================================== #
# ++++++++++++++++++++|      market/news      |+++++++++++++++++++++++++ #
# ====================================================================== #
""" Recently published stock news in all sectors. Returned as a json scheme, 
with a number being the as the key and inside they have a dictionary 
containing 5 key, value items. """

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------

import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/ne/news", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------

import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/ne/news"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


# ====================================================================== #
# ++++++++++++++++++++|      insider-trades    |++++++++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/v1/sec/form4", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/v1/sec/form4"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)



# ====================================================================== #
# +++++++++++++++++++|      market/news/{stock}    |++++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------

import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/ne/news/AAPL", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------

import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/ne/news/AAPL"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


# ====================================================================== #
# ++++++++++++++++++|      market/quotes/{stocks}    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL,MSFT", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------

import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL,MSFT"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


# ====================================================================== #
# ++++++++++++++++++++|      stock/combine/data    |++++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/mo/module/AAPL?module=asset-profile%2Cfinancial-data%2Cearnings", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/mo/module/AAPL"

querystring = {"module":"asset-profile,financial-data,earnings"}

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


# ====================================================================== #
# ++++++++++++++++++++++++++|      Options    |+++++++++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/op/option/AAPL?expiration=1655424000", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/op/option/AAPL"

querystring = {"expiration":"1655424000"}

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# ====================================================================== #
# +++++++++++++++++++++++|      stock/profile    |++++++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/asset-profile", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/asset-profile"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


# ====================================================================== #
# ++++++++++++++++++++|      stock/financial-data    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/financial-data", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/financial-data"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


# ====================================================================== #
# ++++++++++++++++++++|      stock/key-statistics   |+++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/default-key-statistics", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/default-key-statistics"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


# ====================================================================== #
# ++++++++++++++++++++|      stock/balance-sheet    |+++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/balance-sheet", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/balance-sheet"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


# ====================================================================== #
# +++++++++++++++++++++++|      stock/history    |++++++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/hi/history/AAPL/15m", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/hi/history/AAPL/15m"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

# ====================================================================== #
# +++++++++++++++++++|      stock/insider-holders    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/insider-holders", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/insider-holders"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


# ====================================================================== #
# +++++++++++++++++++++|      stock/sec-filings    |++++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/sec-filings", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/sec-filings"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

# ====================================================================== #
# +++++++++++++++++|      stock/recommendation-trend    |+++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/recommendation-trend", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/recommendation-trend"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

# ====================================================================== #
# ++++++++++++++|      stock/upgrade-downgrade-history    |+++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/upgrade-downgrade-history", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/upgrade-downgrade-history"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

# ====================================================================== #
# +++++++++++++|      stock/net-share-purchase-activity    |++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/net-share-purchase-activity", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/net-share-purchase-activity"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

# ====================================================================== #
# ++++++++++++++++|      stock/institution-ownership    |+++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/institution-ownership", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/institution-ownership"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

# ====================================================================== #
# ++++++++++++++++|      stock/insider-transactions    |++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/insider-transactions", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/insider-transactions"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

# ====================================================================== #
# +++++++++++++++++++++|      stock/index-trend    |++++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/index-trend", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/index-trend"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

# ====================================================================== #
# ++++++++++++++++++++|      stock/income-statement    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/income-statement", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/income-statement"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

# ====================================================================== #
# ++++++++++++++++++++|      stock/earnings    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/earnings", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/earnings"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

# ====================================================================== #
# ++++++++++++++++++++|      stock/earnings-trend    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/earnings-trend", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/earnings-trend"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

# ====================================================================== #
# ++++++++++++++++++++|      stock/earnings-history    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/earnings-history", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/earnings-history"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

# ====================================================================== #
# ++++++++++++++++++++|      stock/cashflow-statement    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/cashflow-statement", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/cashflow-statement"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

# ====================================================================== #
# ++++++++++++++++++++|      stock/calendar-events    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/calendar-events", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/calendar-events"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

# ====================================================================== #
# ++++++++++++++++++++|      market/most-watched    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/tr/trending", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/tr/trending"

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

# ====================================================================== #
# ++++++++++++++++++++|      market/small_cap_gainers    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/co/collections/small_cap_gainers?start=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/co/collections/small_cap_gainers"

querystring = {"start":"0"}

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# ====================================================================== #
# ++++++++++++++++++++|      market/aggressive_small_caps    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/co/collections/aggressive_small_caps?start=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/co/collections/aggressive_small_caps"

querystring = {"start":"0"}

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# ====================================================================== #
# ++++++++++++++++++++|      market/undervalued_large_caps    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/co/collections/undervalued_large_caps?start=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/co/collections/undervalued_large_caps"

querystring = {"start":"0"}

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# ====================================================================== #
# ++++++++++++++++++++|      market/most_actives    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/co/collections/most_actives?start=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/co/collections/most_actives"

querystring = {"start":"0"}

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# ====================================================================== #
# ++++++++++++++++++++|      market/day_losers    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/co/collections/day_losers?start=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/co/collections/day_losers"

querystring = {"start":"0"}

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# ====================================================================== #
# ++++++++++++++++++++|      market/day_gainers    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/co/collections/day_gainers?start=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/co/collections/day_gainers"

querystring = {"start":"0"}

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# ====================================================================== #
# ++++++++++++++++++++|      market/growth_technology_stocks    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/co/collections/growth_technology_stocks?start=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/co/collections/growth_technology_stocks"

querystring = {"start":"0"}

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
# ====================================================================== #
# ++++++++++++++++++++|      market/undervalued_growth_stocks    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/co/collections/undervalued_growth_stocks?start=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/co/collections/undervalued_growth_stocks"

querystring = {"start":"0"}

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# ====================================================================== #
# ++++++++++++++++++++|      market/top-gainers-depreciated    |++++++++++++++++++ #
# ====================================================================== #
"""

"""

# --------------------------------------------------------------------------
# http.client
# --------------------------------------------------------------------------
import http.client

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/api/yahoo/ga/topgainers?start=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# --------------------------------------------------------------------------
# requests
# --------------------------------------------------------------------------
import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/ga/topgainers"

querystring = {"start":"0"}

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
