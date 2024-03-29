# TODO: IMPROVE SPEED. MAKE THIS AN ASYNCHRONOUS FUNCTION. RIGHT NOW IT TAKES TWO MINUTES TO
# GET ALL THE SYMBOLS FROM THAT ONE WEBSITE.

import requests, os
import string
import pandas as pd
from bs4 import BeautifulSoup as bs
import asyncio, aiohttp, httpx
from loguru import logger

PATH = "./tmp/"
FILE = "scraper.log"
LOG_FILE = os.path.join(PATH, FILE)
logger.add(LOG_FILE, format="{time:MM/DD/YYYY at HH:mm:ss} | {level} | {name} | {message}", diagnose=True, backtrace=True)

def companies():

    exchanges = ["NYSE", "NASDAQ", "AMEX", "OTCBB"]

    columns = ["exchange", "symbol", "name"]

    def get_companies(exchange="NYSE"):

        """
        :param exchange: The Stock exchange for which you want
        to get a current list of all the symbols for.
        Default -> NYSE

        :returns: a list of tuples containing every company name and symbol in
        the market exchange passed to the function
        """

        alpha = list(string.ascii_uppercase)
        symbols = list()
        names = list()
        # loop through the letters in the alphabet to get the stocks on each page
        # from the table and store them in a list
        logger.info("Get stock market tickers for {} exchange", exchange)
        for each in alpha:
            
            url = "http://eoddata.com/stocklist/{}/{}.htm".format(exchange, each)
            resp = requests.get(url)
            site = resp.content
            soup = bs(site, 'html.parser')
            table = soup.find('table', {'class': 'quotes'})
            for row in table.findAll('tr')[1:]:
                symbols.append(row.findAll('td')[0].text.rstrip())
            for row in table.findAll('tr')[1:]:
                names.append(row.findAll('td')[1].text.rstrip())
            logger.info("Extracted tickers from {} for {} exchange", url, exchange)

        clean_symbols = [symbol.replace('.','-').split('-')[0] for symbol in symbols]
        clean_names = [n.replace('.','-').split('-')[0] for n in names]
        logger.info("Cleaned the symbols and names by removing hyphens and additional letters")

        companies = list(zip(clean_symbols, clean_names))
        logger.info("Extracted {} groups of company symbols and names:", len(companies))

        # turn companies list into a set:
        companies = set(companies)
        logger.info("{} left after removing duplicates:", len(companies))

        suffixes = ['Q', 'W', 'C', 'R', 'P', 'F']

        # Create a del_set and save_set
        del_set = set()
        save_set = set()

        for symbol in companies:
            if len(symbol[0]) > 4 and symbol[0][-1] in suffixes:
                del_set.add(symbol)
            else:
                save_set.add(symbol)
        logger.info("Removed {} unqualified symbols:", len(del_set))
        logger.info("Kept {} qualified symbols:", len(save_set))

        return list(save_set)

    logger.info("[+] Begin extracting company information:")
    NYSE = get_companies(exchanges[0])
    NASDAQ = get_companies(exchanges[1])
    AMEX = get_companies(exchanges[2])
    OTCBB = get_companies(exchanges[3])

    logger.info("[+] Add the exchange next to symbol and name")
    NYSE = [("NYSE",) + elem for elem in NYSE]
    NASDAQ = [("NASDAQ",) + elem for elem in NASDAQ]
    AMEX = [("AMEX",) + elem for elem in AMEX]
    OTCBB = [("OTCBB",) + elem for elem in OTCBB]

    NYSE = set(NYSE)
    NASDAQ = set(NASDAQ)
    AMEX = set(AMEX)
    OTCBB = set(OTCBB)

    logger.info("[+] Join the company sets")
    companies = set.union(NYSE, NASDAQ, AMEX, OTCBB)

    companies = list(companies)
    logger.info("[+] Create company dataframe")
    df = pd.DataFrame([x for x in companies], columns=columns)

    # Now check for duplicates and drop them from the main dataset
    logger.info("[+] One last check to drop duplicate symbols and names:")
    df = df.drop_duplicates(
        subset="symbol", keep="first")
    df = df.drop_duplicates(
        subset="name", keep="first")

    logger.success("Retrieved all the company stock symbols and names. Returning a pandas dataframe:")
    return df


# CREATE A FUNCTION THAT ALLOWS THE USER TO INPUT THE SYMBOLS THAT
# THEY WANT TO GET DATA FOR. IT WILL USE INPUT AND WILL HAVE THE 
# USER JUST PUT A COMMA BETWEEN EACH SYMBOL:
def ask_for_symbols():
    """
    :description: ask the user what symbols they would
    like to use to extract market data. They can choose
    one, or a bunch. They just have to seperate each one
    by a comma. (uppercase not required)
    """
    beginning = "| "
    space = " "
    end = "|"
    print("+ "+"="*47+" +")
    print(beginning+"Below you need to input whichever stock"+space*9+end)
    print(beginning+"symbols you want to extract data for."+space*11+end)
    print(beginning+"You dont need to worry about them being"+space*9+end)
    print(beginning+"uppercase. Just make sure they are seperated"+space*4+end)
    print(beginning+"by a comma."+space*37+end)
    print(beginning+"-"*48+end)
    s = input("| Symbols: ")
    s = s.upper().split(',')
    s = [symbol.strip() for symbol in s]
    print(beginning+"-"*48+end)
    print(s)
    print("+ "+"="*47+" +")