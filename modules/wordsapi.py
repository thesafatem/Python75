import requests
import json
import config

word = input()

url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions"

headers = {
    'x-rapidapi-key': config.TOKEN,
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
result = json.loads(response.text)
print(result['definitions'][0]['definition'])
