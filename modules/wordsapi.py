import requests
import json

word = input()

url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions"

headers = {
    'x-rapidapi-key': "c83e7d750dmshcde9415b4bd29b2p1fdd2ajsnc5945f3ce5bb",
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
result = json.loads(response.text)
print(result['definitions'][0]['definition'])
