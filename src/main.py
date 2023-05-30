# Import the argparse module for command-line argument parsing
import argparse

# Import the pandas library for data manipulation and analysis
import pandas as pd

# Import the players and teams modules from the nba_api.stats.static package
# These modules provide static information about NBA players and teams
from nba_api.stats.static import players, teams 

# Import the PlayerCareerStats, TeamDetails, and TeamYearByYearStats modules
# from the nba_api.stats.endpoints package
# These modules provide access to NBA player career stats, team details, and year-by-year stats
from nba_api.stats.endpoints import PlayerCareerStats, TeamDetails, TeamYearByYearStats

def find_player_by_name(name):
    """
    Find player information by name.

    Returns:
        list: List of player dictionaries matching the given name.
    """ 
    player_dict = players.get_players()
    return [player for player in player_dict if player['full_name'] == name]

def find_team_by_name(name):
    """
    Find team information by name.

    Returns:
        list: List of team dictionaries matching the given name.
    """ 
    team_dict = teams.get_teams()
    return [team for team in team_dict if team['full_name'] == name]

def get_player_stats(player_id): 
    """
    Get career stats for a player.

    Returns:
        pandas.DataFrame: DataFrame containing the player's career stats.
    """
    career_stats = PlayerCareerStats(player_id=player_id)
    career_stats_df = career_stats.get_data_frames()[0]
    return career_stats_df

def get_team_info(team_id):
    """
    Get details of a team.

    Returns:
        pandas.DataFrame: DataFrame containing the team details.
    """
    team_info = TeamDetails(team_id=team_id)
    team_info_df = team_info.get_data_frames()[0]
    return team_info_df

def get_team_year_by_year_stats(team_id):
    """
    Get year-by-year stats for a team.

    Returns:
        pandas.DataFrame: DataFrame containing the team's year-by-year stats.
    """
    team_stats = TeamYearByYearStats(team_id=team_id)
    team_stats_df = team_stats.get_data_frames()[0]
    return team_stats_df

# Create the argument parser
parser = argparse.ArgumentParser(description='NBA Player and Team Information')
parser.add_argument('--player', help='Find player information by name')
parser.add_argument('--team', help='Find team information by name')

# Parse the arguments
args = parser.parse_args()

if args.player:
    # Player search
    player_name = args.player
    player_info = find_player_by_name(player_name)

    if player_info:
         # Player found, get career stats
        player_id = player_info[0]['id']
        player_stats = get_player_stats(player_id)
        
        print("\nPlayer Information:")
        print(player_info)
        
        print("\nPlayer Career Stats:")
        print(player_stats)
    else:
        # Player not found
        print("Player not found.")

if args.team:
    # Team search
    team_name = args.team
    team_info = find_team_by_name(team_name)

    if team_info:
        # Team found, get team details and year-by-year stats
        team_id = team_info[0]['id']
        team_details = get_team_info(team_id)
        team_details_df = pd.DataFrame(team_details)

        team_year_by_year_stats = get_team_year_by_year_stats(team_id)
        team_year_by_year_stats_df = pd.DataFrame(team_year_by_year_stats)
       
        print("\nTeam Information:")
        print(team_info)
        
        print("\nTeam Details:")
        print(team_details_df)

        print("\nTeam Year-by-Year Stats:")
        print(team_year_by_year_stats_df)
    else:
        # Team not found
        print("Team not found.")