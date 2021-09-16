"""
Iframely API Documentation
Just send us a URL and get oEmbed and data back. 
Connect once and get all the features through the same endpoint.
"""

import http.client

conn = http.client.HTTPSConnection("iframely.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "iframely.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/json?url=%3CREQUIRED%3E", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))