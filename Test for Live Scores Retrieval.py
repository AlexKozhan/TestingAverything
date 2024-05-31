"""This script tests the API endpoint for
fetching live scores, ensuring it returns
a valid response and correct data structure."""

import requests

# Replace with your SportMonks API token
API_TOKEN = 'your_api_token_here'

# Endpoint for live scores
url = 'https://api.sportmonks.com/v3/football/livescores/now'

# Parameters including your API token
params = {
    'api_token': API_TOKEN
}


# Test live scores API
def test_live_scores():
    response = requests.get(url, params=params)
    assert response.status_code == 200, "API request failed"

    data = response.json()
    assert 'data' in data, "Data not found in response"

    for match in data['data']:
        assert 'home_team' in match and 'away_team' in match, "Teams data missing"
        assert 'scores' in match, "Scores data missing"

    print("Live scores API test passed!")


test_live_scores()
