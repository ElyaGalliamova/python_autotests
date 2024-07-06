import requests
import pytest


url = 'https://api.pokemonbattle.ru/v2'
token = '26980599f63dfe0e232f24ff93a826a1'
header = {'Content-Type' : 'application/json', 'trainer_token': token}
trainer_id = 6322

def test_status():
    response = requests.get(url = f'{url}/trainers')
    assert response.status_code == 200


def test_part_of_response():
    response = requests.get(url = f'{url}/trainers')
    assert response.json()['data'][0]['id'] == '6322'