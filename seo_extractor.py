#!/usr/bin/mlenv2 python

# TODO: IMPORT ALL REQUIRED PACKAGES
import requests


# HEADERS NEEDED FOR THE RETURN FUNCTION (CONTAINS CONTENT TYPE, KEY, AND HOST)
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "canssens-seo-extraction-v1.p.rapidapi.com",
    'x-rapidapi-key': "292e5f6756msh0abb3103cb293b6p189764jsn96d2fc366bde"
    }

# TODO: ALLOW USER INPUT FOR THE WEBSITE THEY WANT SEO DATA FROM
# PAYLOAD IS THE WEB PAGE YOU WANT THE SEO FOR
payload = "url=" + input("Paste the webpage you want to receive SEO data for: ")

# TODO: CREATE A FUNCTION TO CALL 
def main(headers, payload):

    # url for API call 
    url = "https://canssens-seo-extraction-v1.p.rapidapi.com/seo/api/"

    # API response
    response = requests.request("POST", url, data=payload, headers=headers)

    # print the response text 
    print(response.text)



# TODO: ADD if __name__ == "__main__": TO MAKE THIS SCRIPT CALLABLE

if __name__ == '__main__':
    main(headers, payload)


