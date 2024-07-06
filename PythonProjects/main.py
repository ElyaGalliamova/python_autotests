import requests

url = 'https://api.pokemonbattle.ru/v2'
token = '26980599f63dfe0e232f24ff93a826a1'
header = {'Content-Type' : 'application/json', 'trainer_token': token}
body_pokemons = { "name": "RDS gp",
    "photo_id": 5
}
body_pokemon_change = {
    "pokemon_id": "41969",
    "name": "RDS GP",
    "photo_id": 5
}

body_pokeball = {
    "pokemon_id": "41970"
}

'''response = requests.post(url = f'{url}/pokemons', headers = header, json = body_pokemons)
print(response.text)'''

'''response = requests.put(url = f'{url}/pokemons', headers = header, json = body_pokemon_change)
print(response.text)'''

response = requests.post(url = f'{url}/trainers/add_pokeball', headers = header, json = body_pokeball)
print(response.text)