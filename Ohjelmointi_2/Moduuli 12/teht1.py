import requests

vastaus = requests.get("https://api.chucknorris.io/jokes/random")
if vastaus.status_code == 200:
    data = vastaus.json()
    print(data["value"])
else:
    print("error")