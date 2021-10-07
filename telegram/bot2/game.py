import requests
import json


class Game:
    def __init__(self):
        url = "https://wordsapiv1.p.rapidapi.com/words/"
        querystring = {"random": "true"}
        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': "c83e7d750dmshcde9415b4bd29b2p1fdd2ajsnc5945f3ce5bb"
        }
        while True:
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = json.loads(response.text)
            word = data['word']
            if word.isalpha():
                self.word = word
                self.guessed = ['_' for _ in range(len(word))]
                self.lives = 9
                self.tried = []
                self.active = True
                return

    def guess(self, letter):
        letter = letter.lower()
        if letter in self.tried:
            return {
                "message": "You have already guessed this letter",
                "word": self.get_guessed_word()
            }
        else:
            self.tried.append(letter)
            if letter in self.word:
                for i in range(len(self.word)):
                    if self.word[i] == letter:
                        self.guessed[i] = letter
                if '_' not in self.guessed:
                    self.active = False
                    return {
                        "message": "You win",
                        "word": self.word
                    }
                return {
                    "message": "You guessed correctly",
                    "word": self.get_guessed_word()
                }
            else:
                self.lives -= 1
                if self.lives == 0:
                    self.active = False
                    return {
                        "message": "You died",
                        "word": self.word
                    }
                else:
                    return {
                        "message": "You guessed incorrectly",
                        "word": self.get_guessed_word()
                    }

    def get_guessed_word(self):
        return ''.join(self.guessed)
