# Importing the unittest module for writing test cases
import unittest

# Importing necessary classes from unittest.mock module for mocking
from unittest.mock import patch, MagicMock

# Importing pandas library for working with data frames
import pandas as pd

# Importing functions from the main module
from main import find_player_by_name, find_team_by_name, get_player_stats, get_team_info, get_team_year_by_year_stats

class NBACliTest(unittest.TestCase):
    def test_find_player_by_name(self):
        """
        Test the find_player_by_name function.
        """
         # Prepare test data
        player_dict = [{'full_name': 'LeBron James'}, {'full_name': 'Stephen Curry'}]
        
         # Mock the get_players function and verify the result
        with patch('main.players.get_players', return_value=player_dict):
            result = find_player_by_name('LeBron James')
            self.assertEqual(result, [{'full_name': 'LeBron James'}])

    def test_find_team_by_name(self):
        """
        Test the find_team_by_name function.
        """
         # Prepare test data
        team_dict = [{'full_name': 'Los Angeles Lakers'}, {'full_name': 'Golden State Warriors'}]
        
         # Mock the get_teams function and verify the result
        with patch('main.teams.get_teams', return_value=team_dict):
            result = find_team_by_name('Los Angeles Lakers')
            self.assertEqual(result, [{'full_name': 'Los Angeles Lakers'}])

    def test_get_player_stats(self):
        """
        Test the get_player_stats function.
        """
        
        # Prepare test data
        player_id = '123'
        career_stats_mock = MagicMock()
        career_stats_mock.get_data_frames.return_value = [pd.DataFrame({'player_id': ['123'], 'points': [25]})]
       
        # Mock the PlayerCareerStats class and verify the result
        with patch('main.PlayerCareerStats', return_value=career_stats_mock):
            result = get_player_stats(player_id)
            expected_df = pd.DataFrame({'player_id': ['123'], 'points': [25]})
            pd.testing.assert_frame_equal(result, expected_df)

    def test_get_team_info(self):
        """
        Test the get_team_info function.
        """
       
        # Prepare test data
        team_id = '456'
        team_info_mock = MagicMock()
        team_info_mock.get_data_frames.return_value = [pd.DataFrame({'team_id': ['456'], 'name': ['Los Angeles Lakers']})]
        
         # Mock the TeamDetails class and verify the result
        with patch('main.TeamDetails', return_value=team_info_mock):
            result = get_team_info(team_id)
            expected_df = pd.DataFrame({'team_id': ['456'], 'name': ['Los Angeles Lakers']})
            pd.testing.assert_frame_equal(result, expected_df)

    def test_get_team_year_by_year_stats(self):
        """
        Test the get_team_year_by_year_stats function.
        """
        # Prepare test data
        team_id = '789'
        team_stats_mock = MagicMock()
        team_stats_mock.get_data_frames.return_value = [pd.DataFrame({'team_id': ['789'], 'season': ['2020-2021'], 'wins': [50], 'losses': [22]})]
        
        # Mock the TeamYearByYearStats class and verify the result
        with patch('main.TeamYearByYearStats', return_value=team_stats_mock):
            result = get_team_year_by_year_stats(team_id)
            expected_df = pd.DataFrame({'team_id': ['789'], 'season': ['2020-2021'], 'wins': [50], 'losses': [22]})
            pd.testing.assert_frame_equal(result, expected_df)

if __name__ == '__main__':
    unittest.main()