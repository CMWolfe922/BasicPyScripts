# CRYPTO NEWS API RAPID API

#HTTP CLIENT
import http.client

conn = http.client.HTTPSConnection("crypto-news5.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "crypto-news5.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

conn.request("GET", "/", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


# REQUESTS
import requests

url = "https://crypto-news5.p.rapidapi.com/"

headers = {
    'x-rapidapi-host': "crypto-news5.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)