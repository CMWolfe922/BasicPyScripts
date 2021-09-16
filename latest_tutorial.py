#!/usr/bin/env python3

# THIS SCRIPT DOWNLOADS THE LATEST TUTORIAL FROM REAL PYTHON

from reader import feed 
import time

def main():
	"""Download and print the latest tutorial from Real Python"""
	tic = time.perf_counter() # time code execution
	tutorial = feed.get_article(0)
	toc = time.perf_counter() 
	print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")

	print(tutorial)

if __name__ == "__main__":
	main()

