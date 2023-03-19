# We’re going to start simple by scraping a list of reviews for episodes
# of a TV series, using IMDB (the Internet Movie Database). We’ll use Game of Thrones as
# an example, the episode list for which can be found at http://www.imdb.com/title/
# tt0944947/episodes

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'http://www.imdb.com/title/tt0944947/episodes'
episodes = []
ratings = []

# Go over seasons 1 to 8
for season in range(1, 9):
    r = requests.get(url, params={'season': season})
    soup = BeautifulSoup(r.text, 'html.parser')
    listing = soup.find('div', class_='eplist')
    for epnr, div in enumerate(listing.find_all('div', recursive=False)):
        episode = "{}.{}".format(season, epnr + 1)
        rating_el = div.find(class_='ipl-rating-star__rating')
        rating = float(rating_el.get_text(strip=True))
        print('Episode:', episode, '-- rating:', rating)
        episodes.append(episode)
        ratings.append(rating)


episodes = ['S' + e.split('.')[0] if int(e.split('.')[1]) == 1 else '' for e in episodes]
plt.figure()
positions = [a*2 for a in range(len(ratings))]
plt.bar(positions, ratings, align='center')
plt.xticks(positions, episodes)
plt.show()