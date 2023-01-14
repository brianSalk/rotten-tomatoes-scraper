# rotten-tomatoes-scraper
A python webscraper that uses selenium, requests and BeautifulSoup to scrape rottentomatoes.com 
## How to use
**0)** make sure you have python3.x, selenium, and BeautifulSoup installed on your computer. \
**1)** clone this repo to your computer by opening a UNIX terminal and entering the following `git clone https://github.com/brianSalk/rotten-tomatoes-scraper.git` \
**2)** change into the directory that you just cloned to your computer `cd rotten-tomatoes-scraper` \
**3)** run the script called `scrape.py` with the command `python scrape.py` 

### What it does:
Uses python to the *N* most recent movies that were rated on Rotton Tomatoes. \
After it has found the titles of the movies, it scrapes reviews. \
reveiws are calculated by counting the number of stars the are either full, half, or empty. \
lastly, it will produce a 2D python list where reviews[i][0] is the text of the ith review and reviews[i][1] is the numeric rating of the ith review. \


