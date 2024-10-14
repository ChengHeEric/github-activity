import aiohttp
import asyncio
import pandas as pd

# Function to send a single GET request with headers
async def fetch(session, url, headers):
    async with session.get(url, headers=headers) as response:
        return await response.json()  # Or response.json() for JSON responses

# Function to send multiple GET requests concurrently, with headers
async def fetch_all(urls, headers):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch(session, url, headers))  # Create a task for each URL with headers
        responses = await asyncio.gather(*tasks)  # Run all tasks concurrently
        return responses

api_key = '9444122f-110e-4f4e-81fb-5162e1c70cac'
api_name = 'Key_FhNKALzMPk'

headers = {"Authorization": f"Bearer {api_key}"}

#read the csv file
df = pd.read_csv('faceit_analysis\player_match_history.csv')

#convert the data frame to a list
data = df.values.tolist()

team_1_player_1 = asyncio.run(fetch_all(data[0][1:], headers))
team_1_player_2 = asyncio.run(fetch_all(data[1][1:], headers))
team_1_player_3 = asyncio.run(fetch_all(data[2][1:], headers))
team_1_player_4 = asyncio.run(fetch_all(data[3][1:], headers))
team_1_player_5 = asyncio.run(fetch_all(data[4][1:], headers))
team_2_player_1 = asyncio.run(fetch_all(data[5][1:], headers))
team_2_player_2 = asyncio.run(fetch_all(data[6][1:], headers))
team_2_player_3 = asyncio.run(fetch_all(data[7][1:], headers))
team_2_player_4 = asyncio.run(fetch_all(data[8][1:], headers))
team_2_player_5 = asyncio.run(fetch_all(data[9][1:], headers))

stats_sum = []

def get_stats(matches, playernumber):
    
    for i in matches:

        round_stats = i['rounds'][0]['round_stats']
        
        map = round_stats['Map']
        
        score = round_stats['Score']
        
        winner = round_stats['Winner']
        
        team_1_roster_playerr_id = []
                
        for j in i['rounds'][0]['teams'][0]['players']:
            team_1_roster_playerr_id.append(j['player_id'])
        if winner == i['rounds'][0]['teams'][0]['team_id'] and data[0][0] in team_1_roster_playerr_id:
            win_loss = 1
        else:
            win_loss = 0
        
        for team in i['rounds'][0]['teams']:
            for player in team['players']:
                if data[0][0] == player['player_id']:
                    global player_stats
                    player_stats = player['player_stats']
        
        adr = player_stats['ADR']
        
        kd_ratio = player_stats['K/D Ratio']
        
        enemies_flashed_per_round = player_stats['Enemies Flashed per Round in a Match']
        
        flashes_per_round_in_a_match = player_stats['Flashes per Round in a Match']
        
        entry_entry_rate = player_stats['Match Entry Rate'] 
        
        match_entry_win_rate = player_stats['Match Entry Success Rate']
        
        sniper_kill_rate_per_match = player_stats['Sniper Kill Rate per Match']
        
        utility_usage_per_round = player_stats['Utility Usage per Round']
        
        utility_damage = player_stats['Utility Damage']
        
        #create a dictionary

        stats = {'player_id':data[playernumber][0],'match_id':i['rounds'][0]['match_id'],'map':map,'win/loss':win_loss, 'adr':adr,'kd_ratio':kd_ratio,'enemies_flashed_per_round':enemies_flashed_per_round,'flashes_per_round_in_a_match':flashes_per_round_in_a_match,'entry_entry_rate':entry_entry_rate,'match_entry_win_rate':match_entry_win_rate,'sniper_kill_rate_per_match':sniper_kill_rate_per_match,'utility_usage_per_round':utility_usage_per_round,'utility_damage':utility_damage}
        
        #insert the stats dictionary into a bigger dictionary
        stats_sum.append(stats)


get_stats(team_1_player_1,0)
get_stats(team_1_player_2,1)
get_stats(team_1_player_3,2)
get_stats(team_1_player_4,3)
get_stats(team_1_player_5,4)
get_stats(team_2_player_1,5)
get_stats(team_2_player_2,6)
get_stats(team_2_player_3,7)
get_stats(team_2_player_4,8)
get_stats(team_2_player_5,9)

#convert stats_sum to a dataframe
df = pd.DataFrame(stats_sum)

#save the dataframe to a csv file
df.to_csv('faceit_analysis\output.csv', index=False)
