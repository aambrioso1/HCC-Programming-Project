# /hcc-programming-project/nhl_api.py
"""
We use the API found here: https://statsapi.web.nhl.com/api/v1/teams
to extract information for a web page.

See this article:

https://hackernoon.com/retrieving-hockey-stats-from-the-nhls-undocumented-api-zz3003wrw

First part of the online NHL API
https://statsapi.web.nhl.com/api/v1/teams/teams/{int}
0: None
1: New Jersey Devils
2: New York Islanders
3: New York Rangers
4: Philadelphia Flyers

"""

import requests, json, time

# This dictionary was created by hand.
teams_dict = {
	1: 'New Jersey Devils', 2: 'New York Islanders', 3: 'New York Rangers',\
	4: 'Philadelphia Flyers', 5: 'Pittsburgh Penguins', 6: 'Boston Bruins', \
	7: 'Buffalo Sabres', 8: 'Montréal Canadiens', 9: 'Ottawa Senators', \
 	10: 'Toronto Maple Leafs', 11: 'Carolina Hurricanes', 12: 'Florida Panthers', \
 	13: 'Tampa Bay Lightning', 14: 'Washington Capitals', 15: 'Chicago Blackhawks', \
 	16: 'Detroit Red Wings', 17: 'Nashville Predators', 18: 'St. Louis Blues', \
 	19: 'Calgary Flames', 20: 'Colorado Avalanche', 21: 'Edmonton Oilers', \
 	22: 'Vancouver Canucks', 23: 'Anaheim Ducks', 24: 'Dallas Stars', \
 	25: 'Los Angeles Kings', 26: 'San Jose Sharks', 27: 'Columbus Blue Jackets', \
 	28: 'Minnesota Wild', 29: 'Winnipeg Jets', 30: 'Arizona Coyotes', \
 	31: 'Vegas Golden Knights', 32: 'Seattle Kraken'}

url = 'https://statsapi.web.nhl.com/api/v1/teams/' # URL for team data provided by the NHL
response = requests.get(url)
response.raise_for_status() # Verifies that we get a good response.

# Load json data into a Python variable.
data = json.loads(response.text)

# This creates a dictionary, new_teams_dict[int_id] = 'team_name', using the online API.
new_teams_dict = dict()
for i in range(1, len(data['teams'])+1):
	new_teams_dict[i] = data['teams'][i-1]['name']

print(f'{teams_dict=}')
print(f'{new_teams_dict=}')

