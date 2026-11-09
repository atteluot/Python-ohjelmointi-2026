import requests

nimi = input("Anna paikkakunnan nimi: ").strip()
osoite = f"https://wttr.in/{nimi},finland?format=3"
vastaus = requests.get(osoite)

if vastaus.status_code == 200:
    print("\n" + vastaus.text.strip())
else:
    print("Säätietoja ei löydy.")
