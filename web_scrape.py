from gazpacho import get, Soup
import pandas as pd

url = 'https://www.espn.com/nba/team/schedule/_/name/tor/seasontype/2'
html = get(url)
soup = Soup(html)
links = soup.find("a")[1:-4]
game_links = []


for a in links:
    if "gameId" in a.attrs['href']:
        game_links.append(a.attrs['href'])


def add_game(score_list):
    OT = None
    if len(score_list) == 5:
        OT = int(score_list[4].text)

    
    data.append({
        'first' : int(score_list[0].text),
        'second' : int(score_list[1].text),
        'third' : int(score_list[2].text),
        'fourth' : int(score_list[3].text),
        'OT' : OT
    })

def get_scores(table, overtime):
    find_team = table.find("td", { "class" : "team-name"})
    if find_team[0].text == 'TOR':
        add_game(table.find("td")[1 : 5 if not overtime else 6])
    else:
        add_game(table.find("td")[7 if not overtime else 8 : 11 if not overtime else 12])

data = []


def collect_games():
    for link in game_links:
        url = link
        html = get(url)
        soup = Soup(html)
        teams = soup.find("tbody")
        is_overtime = "OT" in soup.find("span", {"class" : "status-detail"}).text
        get_scores(teams[0], is_overtime)

collect_games()  
    
print(data)




