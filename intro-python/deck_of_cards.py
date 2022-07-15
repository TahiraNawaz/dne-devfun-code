import requests

url = "https://deckofcardsapi.com/api/deck/m76yqbycubnj/draw/?count=6"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
