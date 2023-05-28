import argparse
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import PlayerCareerStats

def find_player_by_name(name):
    player_dict = players.get_players()
    return [player for player in player_dict if player['full_name'] == name]

def get_player_stats(player_id):
    career_stats = PlayerCareerStats(player_id=player_id)
    career_stats_df = career_stats.get_data_frames()[0]
    return career_stats_df

parser = argparse.ArgumentParser(description='NBA Player and Team Information')
parser.add_argument('--player', help='Find player information by name')
parser.add_argument('--team', help='Find team information by name')

args = parser.parse_args()

if args.player:
    player_name = args.player
    player_info = find_player_by_name(player_name)

    if player_info:
        player_id = player_info[0]['id']
        player_stats = get_player_stats(player_id)
        
        print("\nPlayer Information:")
        print(player_info)
        
        print("\nPlayer Career Stats:")
        print(player_stats)
    else:
        print("Player not found.")






























# API_KEY = "e5561d3508mshb98ab3b1bb41ee9p1db2fajsnaa596ea7875b"
# def get_player_stats(player_name):
#     url = f"https://free-nba.p.rapidapi.com/players/{player_name}"

#     query_params = {
#         "search": player_name,
#         "page": "0",
#         "per_page": "25"
#     }

#     headers = {
#         "X-RapidAPI-Key": API_KEY,
#         "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
#     }
    
#     response = requests.get(url, headers=headers, params=query_params)
#     print(response.json())  
    
    # if response.status_code == 200:
    #     player_stats = response.json()
    #     return player_stats
    # else:
    #     print("Failed to fetch player statistics.")
    #     return None
    

# if __name__ == '__main__':
#     main()