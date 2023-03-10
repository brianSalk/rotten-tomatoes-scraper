import requests
import pickle
from get_movies import get_movies, print_movies
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import sys
import argparse
options = Options()
options.headless = True


TITLE_LIMIT = float('inf')
OUT_FILE = ""
# do argparse stuff
parser = argparse.ArgumentParser()
parser.add_argument('-o','--out-file', type=str,default='out', help='name of file to store pickled data')
parser.add_argument('-n','--title-limit', type=int,default=100, help='limit number of titles')
parser.add_argument('-b', '--browser', type=str, default='firefox', help='select browser to scrape with')
args = parser.parse_args()
# end argparse stuff
if args.browser.lower() == 'firefox':
    driver = webdriver.Firefox(options=options)
elif args.browser.lower() == 'chrome':
    driver = webdriver.Chrome(options=options)

reviews = []
movie_titles = get_movies(args.title_limit)
for movie in movie_titles:
    has_next_button = True
    url = f'https://www.rottentomatoes.com/m/{movie}/reviews?type=user'
    test_response = requests.get(url)
    if test_response.status_code != 200:
        print(f'{url} is not valid')
        continue
    print(f'scraping {movie}')
    driver.get(url)
    button_class='prev-next-paging__button-right'
    btn = True
    try:
        btn = driver.find_element(By.CLASS_NAME,button_class)
    except Exception:
        has_next_button = False
    page_n=1
    while has_next_button:
        print(page_n)
        for div in driver.find_elements(By.CLASS_NAME, 'audience-reviews__review-wrap'):
            html = None
            try:
                html = div.get_attribute('innerHTML')
            except Exception:
                print('skipping current rating due to error')
                continue
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.find('p', {'class': 'audience-reviews__review'}).text
            rating = 0
            stars = soup.find('span', {'class':'star-display'})
            #print(text)
            
            for star in stars:
                star = star.get('class')
                if star == ['star-display__filled']:
                    rating += 1
                elif star == ['star-display__half']:
                    rating += .5
                elif star == ['star-display__empty']:
                    continue
                else:
                    print('----------invalid star display')
            reviews.append((text,rating))
        try:
            btn = driver.find_element(By.CLASS_NAME, button_class)
            btn.click()
        except Exception:
            has_next_button = False
        page_n+=1

with open(args.out_file, 'wb') as f:
    pickle.dump(reviews, f)
