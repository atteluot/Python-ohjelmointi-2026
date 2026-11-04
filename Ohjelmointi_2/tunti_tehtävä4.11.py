import requests
nimi=input("Anna Pokemoni nimi: ").strip().lower()

vastaus = requests.get("https://pokeapi.co/api/v2/pokemon/"+nimi)
if vastaus.status_code == 200:
    data = vastaus.json()
    for tyyppi in data["types"]:
        print(tyyppi["type"]["name"])
else:
    print("Pokemonia ei löytynyt")