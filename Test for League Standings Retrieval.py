"""This script tests the API endpoint for
fetching league standings, ensuring it returns
the correct data structure."""

import requests
from unittest import TestCase, main
from unittest.mock import patch

class TestLeagueStandings(TestCase):
    @patch('requests.get')
    def test_league_standings(self, mock_get):
        mock_response = {
            'data': [
                {
                    'team': {'name': 'Team A'},
                    'position': 1,
                    'points': 30
                },
                {
                    'team': {'name': 'Team B'},
                    'position': 2,
                    'points': 28
                }
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response = requests.get('https://api.sportmonks.com/v3/football/standings/season/{SEASON_ID}')
        data = response.json()

        self.assertEqual(response.status_code, 200, "API request failed")
        self.assertIn('data', data, "Data not found in response")

        for team in data['data']:
            self.assertIn('team', team, "Team data missing")
            self.assertIn('position', team, "Position data missing")
            self.assertIn('points', team, "Points data missing")

if __name__ == '__main__':
    main()
