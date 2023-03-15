from pytz import timezone
import requests, os, json
import pandas as pd
from loguru import logger
import time
from datetime import datetime
import asyncio

# ================================================================= #
# This allows me to import secret data from a file on my computer 
# from anywhere.
# ----------------------------------------------------------------- #
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:/build')
import acctInfo
# ================================================================= #

# API Data
from acctInfo import TDA_APIKEY
TDA_BASE = "https://api.tdameritrade.com/v1/"

today = datetime.today().astimezone(timezone("America/Chicago"))
today_fmt = today.strftime("%m-%d-%Y")
PATH = "tmp/"
FILE = "tda_stockdata.log"
LOG_FILE = os.path.join(PATH, FILE)
logger.add(LOG_FILE, format="{time:MM/DD/YYYY at HH:mm:ss} | {level} | {name} | {message}", diagnose=True, backtrace=True, enqueue=True, catch=True)



# DATE BUILDING AND MANAGEMENT
# today = datetime.today().astimezone(timezone("America/Chicago"))
# today_fmt = today.strftime("%m-%d-%Y")
# # CREATE THE LOGGER FOR THIS SCRIPT:
# log_path = str(os.path.pardir) + '/logs/'
# base_fmt = "[{time:YYYY-MM-DD at HH:mm:ss}]|[{name}-<lvl>{message}</lvl>]"
# logger.add(log_path+"quotes.log", rotation="2 MB",
#            colorize=True, enqueue=True, catch=True)


class Stock:
    def __init__(self, stocks: list):
        self.stocks = stocks
        self.stock_chunks = self.chunks(stocks) # Chunks the stock list upon instantiation
        # self.engine = create_marketdata_engine() # Creates a database connection engine upon instantiation

        # This function chunks the list of symbols into groups of 200
    def chunks(self, l: list, n: int = 200):
        """
        :param l: takes in a list
        :param n: Lets you know how long you want each chunk to be
        """
        n = max(1, n)
        logger.info("[+] Stocks chunked into groups of 200..")
        return (l[i: i + n] for i in range(0, len(l), n))

    def execute_function(self, func):
        """
        :Description: Main method to obtain Quote data for every stock in the stocks list
        passed to the Quotes() class when instantiated. This method will execute the
        Quote.data method using a chunked stocks list.
        """
        logger.info("[-] Executing the data function on each stock symbol")
        try:
            func_data = pd.concat([func(each)
                                   for each in self.stock_chunks])
            logger.info("[+] Function data retrieved")
            return pd.DataFrame(func_data)

        except Exception as e:
            logger.error("Error Caused Due to {}", e)

def fundamentals(stock):
    """
    :param stocks: List of stocks chunked into 200 symbol chunks
    :return: This will return tons of information that will then
    be changed into dataframes and inserted into the database.
    """
    url = TDA_BASE + "instruments"

    # pass params
    params = {"apikey": TDA_APIKEY, "symbol": stock,
              "projection": "fundamental"}

    request = requests.get(url=url, params=params).json()

    time.sleep(1)

    # create df
    _df = pd.DataFrame.from_dict(
        request, orient="index").reset_index(drop="True")

    def _reshape_fundamentals(df):

        _fund_list = list(df["fundamental"])
        _df = pd.DataFrame([x for x in _fund_list])
        return _df

    df = _reshape_fundamentals(_df)

    return df

def quotes(stock):
    """
    :param stock: a stock symbol
    :return: raw json data to be passed to the
    """
    url = TDA_BASE + "marketdata/quotes"  # market data url
    params = {"apikey": TDA_APIKEY, "symbol": stock}
    request = requests.get(url=url, params=params).json()

    time.sleep(1)  # set sleep so that api works

    # create df
    df = pd.DataFrame.from_dict(
        request, orient="index").reset_index(drop=True)

    # Quote Data: formatting the dates and other columns
    # Now I need to add the dates and format the dates for the database
    df["date"] = pd.to_datetime(today_fmt)
    df["date"] = df["date"].dt.date
    df["divDate"] = pd.to_datetime(df["divDate"])
    df["divDate"] = df["divDate"].dt.date

    # Remove anything without a price
    df = df.loc[df["bidPrice"] > 0]

    # Rename columns, They can't start with a number
    df = df.rename(
        columns={"52WkHigh": "_52WkHigh", "52WkLow": "_52WkLow"})

    return df

