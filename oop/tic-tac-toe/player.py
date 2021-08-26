class Player:
    def __init__(self, symbol, field):
        self.symbol = symbol
        self.field = field

    def make_move(self):
        while True:
            try:
                x, y = map(int, input("Please enter coordinates\n").split())
                self.field.fill((x, y), self.symbol)
                return
            except ValueError:
                print("Invalid coordinates")


