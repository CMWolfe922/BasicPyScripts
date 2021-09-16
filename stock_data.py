# THIS SCRIPT IS USING A YAHOO FINANCE API 
# THAT ONLY ALLOWS 500 CALLS PER MONTH
# I NEED TO TRACK HOW MANY CALLS I MAKE 

# TODO: IMPORT ALL REQUIRED PACKAGES
import requests
from timer import Timer

headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

symbol = input("Type in Company symbol: ")

# TODO: CREATE FUNCTION TO GET COMBINED STOCK DATA: 
def main(symbol, headers):
    t.start()

    url = f"https://yahoo-finance15.p.rapidapi.com/api/yahoo/mo/module/{symbol}"

    querystring = {"module":"asset-profile,financial-data,earnings"}

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

if __name__ == '__main__':
    t = Timer()
    main(symbol, headers)
    t.stop()