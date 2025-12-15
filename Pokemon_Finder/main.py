import requests

def get_pokemon_data(pokemon_name):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon_name)
    if response.status_code == 200:
        return response.json()
    print("Pokémon not found. Please check the name and try again.")
    return None

def display_pokemon_info(data):
    if data is None:
        return None
    print(f"\nName: {data['name']}")
    print("Types:", ", ".join(t['type']['name'] for t in data['types']))
    print("Abilities:", ", ".join(a['ability']['name'] for a in data['abilities']))

    print("Stats:")
    for stat in data['stats']:
        print(f" - {stat['stat']['name']}: {stat['base_stat']}")

while True:
    pokemon_name = input("Pokemon Name: ").lower().strip()
    if pokemon_name == "q":
        print("Bye Bye..")
        break
    pokemon_data = get_pokemon_data(pokemon_name)
    display_pokemon_info(pokemon_data)
    print("\n")