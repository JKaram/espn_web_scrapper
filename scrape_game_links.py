from gazpacho import get, Soup
import pandas as pd

url = 'https://www.espn.com/nba/team/schedule/_/name/tor/seasontype/2'
html = get(url)
soup = Soup(html)
links = soup.find("a")[1:]
game_links = []


for a in links:
    if "gameId" in a.attrs['href']:
        game_links.append(a.attrs['href'])


print(game_links)