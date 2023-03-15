# importing libraries and packages
import snscrape.modules.twitter as snt
import pandas as pd
from datetime import datetime, timedelta
from decorators import timeit

# Get yesterdays date to use in the since param
since_yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')


@timeit
def search_twitter(symbol: str, n: int, since: str = 'yesterday'):
	"""
	:param symbol: Stock symbol to search tweets for.
	:purpose: Search twitter for tweets about each stock symbol
	so that I can get the sentiment analysis on each stock and 
	determine if the stock will go up or down.
	:returns: Pandas DataFrame. 
	"""
	tweets = []
	# if since is yesterday, it goes with the pre formatted yesterday's date. 
	# but if it is a custom date, it uses that.
	if since == 'yesterday':
		for i, tweet in enumerate(snt.TwitterSearchScraper(f'{symbol} since:{since_yesterday}').get_items()):
			if i > n:
				break
			tweets.append([tweet.date, tweet.id, tweet.rawContent, tweet.hashtags, tweet.user.username])
	else: # use the custom date passed to the function.
		for i, tweet in enumerate(snt.TwitterSearchScraper(f'{symbol} since:{since}').get_items()):
			if i > n:
				break
			tweets.append([tweet.date, tweet.id, tweet.rawContent, tweet.hashtags, tweet.user.username])

	return pd.DataFrame(tweets, columns=['datetime', 'tweet_id', 'rawContent', 'hashtags', 'username'])
