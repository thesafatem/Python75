from field import Field
from player import Player
from bot import Bot
from checker import Checker
from random import randint

class Game:
    def play(self):
        field = Field()
        how_many_players = int(input("Please enter the number of players (1 or 2)\n"))
        player1 = None
        player2 = None
        if how_many_players == 1:
            classes = [Player, Bot]
            if randint(0, 1) == 0:
                classes = [Bot, Player]
            player1 = classes[0]('x', field)
            player2 = classes[1]('o', field)
        else:
            player1 = Player('x', field)
            player2 = Player('o', field)

