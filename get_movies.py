import requests
from bs4 import BeautifulSoup
url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/?page='
movies = []
for page_num in range(1,11):
    url += str(page_num)
    result = requests.get('https://www.rottentomatoes.com/browse/movies_in_theaters/')
    soup = BeautifulSoup(result.text, 'html.parser')
    
    for span in soup.find_all('span', {'data-qa':'discovery-media-list-item-title'}):
        title = span.text
        title = title.strip()
        title = title.replace(' ', '_')
        title =title.lower()
        movies.append(title)
def get_movies():
    return movies
def print_movies():
    print(movies)
