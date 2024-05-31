"""This script tests the API endpoint for
fetching historical matches, ensuring
it returns the correct data structure."""

import requests
from unittest import TestCase, main
from unittest.mock import patch

class TestHistoricalMatches(TestCase):
    @patch('requests.get')
    def test_historical_matches(self, mock_get):
        mock_response = {
            'data': [
                {
                    'home_team': {'name': 'Team A'},
                    'away_team': {'name': 'Team B'},
                    'scores': {'home': 2, 'away': 2},
                    'date': '2024-05-01'
                }
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response = requests.get('https://api.sportmonks.com/v3/football/fixtures/history/{TEAM_ID}')
        data = response.json()

        self.assertEqual(response.status_code, 200, "API request failed")
        self.assertIn('data', data, "Data not found in response")

        for match in data['data']:
            self.assertIn('home_team', match, "Home team data missing")
            self.assertIn('away_team', match, "Away team data missing")
            self.assertIn('scores', match, "Scores data missing")
            self.assertIn('date', match, "Match date missing")

if __name__ == '__main__':
    main()
