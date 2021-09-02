from field import Field
from player import Player
from bot import Bot
from checker import Checker
from random import randint

class Game:
    def play(self):
        while True:
            how_many_players = int(input("Please enter the number of players (1 or 2)\n"))

            field_size = int(input("Please enter size of the field\n"))
            field = Field(field_size)
            checker = Checker(field)

            players = [None, None]
            if how_many_players == 1:
                classes = [Player, Bot]
                if randint(0, 1) == 0:
                    classes = [Bot, Player]
                players[0] = classes[0]('x', field)
                players[1] = classes[1]('o', field)
            else:
                players[0] = Player('x', field)
                players[1] = Player('o', field)

            game_over = False
            for i in range(field.size ** 2):
                print(field)
                players[i % 2].make_move()
                if checker.check(players[i % 2]):
                    print(field)
                    print(f"{players[i % 2].symbol} wins")
                    game_over = True
                    break
            if not game_over:
                print(field)
                print("Draw")
            play_again = input("Play again?\n").lower()
            if play_again == 'no':
                break