"""
Basic script that utilizes the reddit package praw. I am trying to
create a script that checks for popular phrases or companies on
CNCB and then search for those phrases in some of reddits top 
subreddits.
"""
# ================================================================= #
# This allows me to import secret data from a file on my computer 
# from anywhere.
# ----------------------------------------------------------------- #
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:/build')

# ================================================================= #

import praw
import acctInfo
from acctInfo import REDDIT_CLIENT_SECRET, REDDIT_CLIENT_ID, REDDIT_USER_AGENT

# GET THE REDDIT OBJ UPON CALLING THIS SCRIPT: 
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)

# NOW THAT I HAVE AN INSTANCE CREATED. I CAN USE IT TO GET THE TOP 
# TEN POSTS FROM A SUBREDDIT. THIS ONE WILL BE THE MACHINE LEARNING SUB REDDIT
hot_ML_posts = reddit.subreddit('MachineLearning').hot(limit=10)

for post in hot_ML_posts:
	print(post.title)


# NOW I CAN GET THE HOTTEST POSTS OF ALL THE SUBREDDITS BY USING 'all'
hottest_posts = reddit.subreddit('all').hot(limit=10)

for posts in hottest_posts:
	print(posts.title)

def extract_text_from_subreddits(subreddits, limit):
	"""
	Check if the subreddits param is a list of subreddits,
	if it is get the length and extract data from each one.
	store the data into a dict with the subreddit as the
	key. 
	"""
	reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)
	if isinstance(subreddits, list):
		data = dict()
		for subreddit in subreddits:
			hot_financial_posts = reddit.subreddit(subreddit).hot(limit=25)
			for post in hot_financial_posts:
				data[subreddit] = {post.title: post.body}

		return data
	else:
		data = dict()
		hot_financial_posts = reddit.subreddit(subreddit).hot(limit=25)
		for post in hot_financial_posts:
			data[subreddit] = {post.title: post.body}
		return data


