import requests
from bs4 import BeautifulSoup
def scrape_titles(n):
    url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/?page='
    movies = []
    for page_num in range(1,n+1):
        url += str(page_num)
        result = requests.get('https://www.rottentomatoes.com/browse/movies_in_theaters/')
        soup = BeautifulSoup(result.text, 'html.parser')
        
        for span in soup.find_all('span', {'data-qa':'discovery-media-list-item-title'}):
            title = span.text
            title = title.strip()
            title = title.replace(' ', '_')
            title =title.lower()
            movies.append(title)
            if len(movies) > n:
                return movies

    return movies
def get_movies(n):
    return scrape_titles(n)
def print_movies():
    print(movies)
