"""This script tests the API endpoint for
fetching upcoming fixtures for a specific team."""

import requests

# Replace with your SportMonks API token
API_TOKEN = 'your_api_token_here'
# Replace with the team ID you want to fetch fixtures for
TEAM_ID = 'your_team_id_here'

# Endpoint for upcoming fixtures by team ID
url = f'https://api.sportmonks.com/v3/football/teams/{TEAM_ID}/fixtures/upcoming'

# Parameters including your API token
params = {
    'api_token': API_TOKEN
}


# Test upcoming fixtures API
def test_upcoming_fixtures():
    response = requests.get(url, params=params)
    assert response.status_code == 200, "API request failed"

    data = response.json()
    assert 'data' in data, "Data not found in response"

    for fixture in data['data']:
        assert 'opponent' in fixture, "Opponent data missing"
        assert 'fixture' in fixture and 'start_date' in fixture['fixture'], "Fixture date missing"

    print("Upcoming fixtures API test passed!")


test_upcoming_fixtures()
