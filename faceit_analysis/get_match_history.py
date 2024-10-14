#import essential libraries
import requests
import pandas as pd

#api key and name 
api_key = '7f8ce17d-1937-4fb4-bd30-7016aff9a038'
api_name = 'Key_GdjvMZvHxQ'

games_url = f'https://open.faceit.com/data/v4/matches/{input("please enter the faceit match id that you want to analyze")}'
headers = {"Authorization": f"Bearer {api_key}"}

response = requests.get(games_url, headers=headers)
print(response.status_code)
data = response.json()
print(data)

# print(data)

team_1_roster_playerr_id = []
team_2_roster_playerr_id = []

#get all players id 
team_1_roster = data['teams']['faction1']['roster']
team_2_roster = data['teams']['faction2']['roster']

for player in team_1_roster:
    team_1_roster_playerr_id.append(player['player_id'])
    
for player in team_2_roster:
    team_2_roster_playerr_id.append(player['player_id'])

#next i will retrive the match history of each player

player_match_history = {}

for player_id in team_1_roster_playerr_id:
    print('analyzing player: ', player_id)
    
    player_url = f"https://open.faceit.com/data/v4/players/{player_id}/history?limit=100"
    response = requests.get(player_url, headers=headers).json()

    matches = []
    for i in response['items']:
        matches.append(f"https://open.faceit.com/data/v4/matches/{i['match_id']}/stats")
    
    player_match_history[player_id] = matches

for player_id in team_2_roster_playerr_id:
    print('analyzing player: ', player_id)
    
    player_url = f"https://open.faceit.com/data/v4/players/{player_id}/history?limit=100"
    response = requests.get(player_url, headers=headers).json()

    matches = []
    for i in response['items']:
        matches.append(f"https://open.faceit.com/data/v4/matches/{i['match_id']}/stats")
    
    player_match_history[player_id] = matches

#export the player match history to a csv file
pd.DataFrame.from_dict(player_match_history, orient='index').to_csv('faceit_analysis\player_match_history.csv')

