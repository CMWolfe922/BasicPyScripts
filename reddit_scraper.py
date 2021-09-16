# THIS SCRIPT ALLOWS ME TO IMPORT MY SECRET DOC HOLDING
# MY USERNAMES AND PASSWORDS
# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:/build')

import praw
import acctInfo
from acctInfo import client_secret, client_id, user_agent

# before I can scrape data from reddit, i need to 
# authenticate myself by creating a reddit instance
reddit = praw.Reddit(client_id=client_id,client_secret=client_secret,user_agent=user_agent)

# NOW THAT I HAVE AN INSTANCE CREATED. I CAN USE IT TO GET THE TOP 
# TEN POSTS FROM A SUBREDDIT. THIS ONE WILL BE THE MACHINE LEARNING SUB REDDIT
hot_ML_posts = reddit.subreddit('MachineLearning').hot(limit=10)

for post in hot_ML_posts:
	print(post.title)


# NOW I CAN GET THE HOTTEST POSTS OF ALL THE SUBREDDITS BY USING 'all'
hottest_posts = reddit.subreddit('all').hot(limit=10)

for posts in hottest_posts:
	print(posts.title)