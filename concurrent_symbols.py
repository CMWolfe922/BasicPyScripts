import string, requests, os
import pandas as pd
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from loguru import logger

"""
This script is an attempt to turn the stock_symbols.py script into an
asynchronous program. The goal is to use concurrency to speed up the
process of extracting stock symbols from the web.
"""

# return each letter in the alphabet
def get_letter_task():
    alpha = list(string.ascii_uppercase)
    for each in alpha:
        yield each

def symbols_extractor_task(exchange, letter):
    symbols = list()
    url = "http://eoddata.com/stocklist/{}/{}.htm".format(exchange, letter)
    resp = requests.get(url)
    site = resp.content
    soup = bs(site, 'html.parser')
    table = soup.find('table', {'class': 'quotes'})
    for row in table.findAll('tr')[1:]:
        symbols.append(row.findAll('td')[0].text.rstrip())
    for row in table.findAll('tr')[1:]:
        names.append(row.findAll('td')[1].text.rstrip())
    logger.info("Extracted tickers from {} for {} exchange", url, exchange)
    return symbols

def symbol_cleaner_task(symbols: list):
    clean_symbols = [symbol.replace('.','-').split('-')[0] for symbol in symbols]
    return clean_symbols