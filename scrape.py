import requests
import pickle
from get_movies import get_movies, print_movies
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import sys
options = Options()
options.headless = True


TITLE_LIMIT = float('inf')
OUT_FILE = ""
for i,arg in enumerate(sys.argv):
    if arg == '-o':
        OUT_FILE = sys.argv[i+1]
    if arg == '-n':
        TITLE_LIMIT = int(sys.argv[i+1])
if TITLE_LIMIT == float('inf'):
    print('please specify a title limit: -n <limit>')
if OUT_FILE == "":
    print('please specify outfile')
    sys.exit(1)
reviews = []
driver = webdriver.Firefox(options=options)
movie_titles = get_movies(TITLE_LIMIT)
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

with open(OUT_FILE, 'wb') as f:
    pickle.dump(reviews, f)
