import requests
from bs4 import BeautifulSoup
def scrape_titles(title_limit = 100,page_limit=100):
    url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/?page='
    movies = []
    for page_num in range(1,page_limit+1):
        url += str(page_num)
        result = requests.get('https://www.rottentomatoes.com/browse/movies_in_theaters/')
        soup = BeautifulSoup(result.text, 'html.parser')
        
        for span in soup.find_all('span', {'data-qa':'discovery-media-list-item-title'}):
            title = span.text
            title = title.strip()
            title = title.replace(' ', '_')
            title =title.lower()
            movies.append(title)
            if len(movies) >= title_limit:
                return movies
    # if title limit is greater than number of films on the site
    return movies
def get_movies(title_limit):
    return scrape_titles(title_limit)
def print_movies():
    print(movies)
