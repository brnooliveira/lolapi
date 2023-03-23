import requests


def get_summoner():
    name = 'Nicknickinho'
    headers = {
        'X-Riot-Token': 'RGAPI-a07db87e-49d7-4238-9a3b-01ea9b0c80f2'
    }
    response = requests.get(
        f'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}', headers=headers)
    summoner_data = response.json()
    return summoner_data


print(get_summoner())
