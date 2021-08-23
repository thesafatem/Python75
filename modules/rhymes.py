import requests
import json

def erase_punctuation_marks(word):
    i = len(word) - 1
    while not word[i].isalpha():
        i -= 1
    return word[:i+1]

file = open('poem.txt', 'r')
poem = file.readlines()
# print(poem)
poem = list(map(lambda x: x.split()[-1], poem))
# print(poem)
poem = list(map(lambda x: erase_punctuation_marks(x).lower(), poem))
# print(poem)

url_13 = f"https://wordsapiv1.p.rapidapi.com/words/{poem[0]}/rhymes"
url_24 = f"https://wordsapiv1.p.rapidapi.com/words/{poem[1]}/rhymes"

headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': "c83e7d750dmshcde9415b4bd29b2p1fdd2ajsnc5945f3ce5bb"
}

response_13 = requests.request("GET", url_13, headers=headers)
response_24 = requests.request("GET", url_24, headers=headers)

data_13 = json.loads(response_13.text)
data_24 = json.loads(response_24.text)

print(poem[0])
for rhyme in data_13['rhymes']['all']:
    print(rhyme, end=', ')
print()

print(poem[1])
for rhyme in data_24['rhymes']['all']:
    print(rhyme, end=', ')
print()

if poem[2] in data_13['rhymes']['all'] \
    and poem[3] in data_24['rhymes']['all']:
    print("POEM")
else:
    print("NOT POEM")