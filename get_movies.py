import requests
from bs4 import BeautifulSoup
<<<<<<< HEAD
def scrape_titles(title_limit = 100,page_limit=100):
    url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/?page='
    movies = []
    for page_num in range(1,page_limit+1):
=======
def scrape_titles(n):
    url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/?page='
    movies = []
    for page_num in range(1,n+1):
>>>>>>> b62271b5435d08644e2d583f332e623386697415
        url += str(page_num)
        result = requests.get('https://www.rottentomatoes.com/browse/movies_in_theaters/')
        soup = BeautifulSoup(result.text, 'html.parser')
        
        for span in soup.find_all('span', {'data-qa':'discovery-media-list-item-title'}):
            title = span.text
            title = title.strip()
            title = title.replace(' ', '_')
            title =title.lower()
            movies.append(title)
<<<<<<< HEAD
            if len(movies) >= title_limit:
                return movies
    # if title limit is greater than number of films on the site
    return movies
def get_movies(title_limit):
    return scrape_titles(title_limit)
=======
            if len(movies) > n:
                return movies

    return movies
def get_movies(n):
    return scrape_titles(n)
>>>>>>> b62271b5435d08644e2d583f332e623386697415
def print_movies():
    print(movies)
