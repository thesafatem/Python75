import requests
import json
import config

url = f"https://wordsapiv1.p.rapidapi.com/words/"

querystring = {'random': "true"}

headers = {
    'x-rapidapi-key': config.TOKEN,
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
result = json.loads(response.text)
print(result)
