from player import Player
from random import randint, randrange, choices, choice


class Bot(Player):
    def __init__(self, symbol, field):
        super().__init__(symbol, field)

    def make_move(self):
        free = []
        for x in range(self.field.size):
            for y in range(self.field.size):
                if self.field.field[x][y] == ' ':
                    free.append((x, y))
        """ 1 вариант как доставать рандомный элемент
        # random_id = randint(0, len(free) - 1)
        random_id = randrange(0, len(free))
        coords = free[random_id]
        """
        """ 2 вариант
        coords = choices(free)[0]
        """
        # 3 вариант
        coords = choice(free)
        self.field.fill(coords, self.symbol)
        print(f"Bot puts {self.symbol} to cell ({coords[0]}, {coords[1]})")
