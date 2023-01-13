import requests
import pickle
from get_movies import get_movies, print_movies
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import sys

page_limit = float('inf')

reviews = []
driver = webdriver.Firefox()
movie_titles = get_movies()
for movie in movie_titles:
    has_next_button = True
    url = f'https://www.rottentomatoes.com/m/{movie}/reviews?type=user'
    test_response = requests.get(url)
    if test_response.status_code != 200:
        print(f'{url} is not valid')
        continue
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
            print(text)
            
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
            break # only read first reveiw
        try:
            btn = driver.find_element(By.CLASS_NAME, button_class)
            btn.click()
        except Exception:
            has_next_button = False
        page_n+=1
        if page_n > page_limit: # only crawl first 'page_limit' pages
            break
with open('reviews', 'wb') as f:
    pickle.dump(reviews, f)
