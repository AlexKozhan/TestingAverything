import requests
from unittest import TestCase, main
from unittest.mock import patch

class TestLiveScores(TestCase):
    @patch('requests.get')
    def test_live_scores(self, mock_get):
        mock_response = {
            'data': [
                {
                    'home_team': {'name': 'Team A'},
                    'away_team': {'name': 'Team B'},
                    'scores': {'home': 1, 'away': 2}
                }
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response = requests.get('https://api.sportmonks.com/v3/football/livescores/now')
        data = response.json()

        self.assertEqual(response.status_code, 200, "API request failed")
        self.assertIn('data', data, "Data not found in response")

        for match in data['data']:
            self.assertIn('home_team', match, "Home team data missing")
            self.assertIn('away_team', match, "Away team data missing")
            self.assertIn('scores', match, "Scores data missing")

if __name__ == '__main__':
    main()
