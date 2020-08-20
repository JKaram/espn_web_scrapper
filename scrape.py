from gazpacho import get, Soup
import pandas as pd

def find_team(box):
    print(type(box))
    output = (box
        .find('div', {'class': 'section_heading'})
        .find('span').attrs['data-label']
        .split(' (')
        [0]
    )
    return output

def parse_player(player, team):
    mp = player.find('td', {'data-stat': 'mp'}).text
    m, s = mp.split(':')
    return {
        'name': player.find('th', {'data-stat': 'player'}).text,
        'team': team,
        'mp': round(float(m) + float(s)/60, 1),
        'pts': int(player.find('td', {'data-stat': 'pts'}).text),
        'a': int(player.find('td', {'data-stat': 'ast'}).text)
    }

def parse_trs(trs, team):
    players = []
    for player in trs[:-1]:
        try:
            players.append(parse_player(player, team))
        except AttributeError:
            pass
    return players

def parse_team(box):
    team = find_team(box)
    trs = box.find('tr')
    data = parse_trs(trs, team)
    return data

def parse_page(game):
    url = f"https://www.basketball-reference.com/boxscores/{game}.html"
    html = get(url)
    soup = Soup(html)
    boxes = (soup
        .find('div', {'id': 'all_box'})
    )
    data = []
    for n in [0, 8]:
        d = parse_team(boxes[n])
        data.extend(d)
    return data

game = '202008140IND'
data = parse_page(game)
df = pd.DataFrame(data)



print(df)

#