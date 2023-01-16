# rotten-tomatoes-scraper
A python webscraper that uses selenium, requests and BeautifulSoup to scrape rottentomatoes.com 
## How to use
**0)** make sure you have python3.x, selenium, and BeautifulSoup installed on your computer. \
**1)** clone this repo to your computer by opening a UNIX terminal and entering the following `git clone https://github.com/brianSalk/rotten-tomatoes-scraper.git` \
**2)** change into the directory that you just cloned to your computer `cd rotten-tomatoes-scraper` \
**3)** run `python scrape.py -o <outfile> -n <num_titles>` 

### What it does:
Retrieves the *N* most recent movies that were rated on Rotton Tomatoes. \
After it has found the titles of the movies, it scrapes reviews. \
reveiws are calculated by counting the number of stars the are either full, half, or empty. \
lastly, it will produce a 2D python list where reviews[i][0] is the text of the ith review and reviews[i][1] is the numeric rating of the ith review. \
The list is stored as a picked python object in the file of your chosing.

### contribute
I want there to be a capability to limit the reviews in various ways. \
Perhaps filter by rating (eg. only scrape polorized reviews, only scrape 4 star reviews etc.) \
Only scrape first N reviews for each movie. \



