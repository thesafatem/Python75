class Checker:
    def __init__(self, field):
        self.field = field

    def check(self, player):
        for i in range(self.field.size):
            ok_row = True
            ok_col = True
            for j in range(self.field.size):
                ok_row = ok_row and self.field.field[i][j] == player.symbol
                ok_col = ok_col and self.field.field[j][i] == player.symbol
            if ok_row or ok_col:
                return True
        ok_1 = True
        ok_2 = True
        for i in range(self.field.size):
            ok_1 = ok_1 and self.field.field[i][i]
            ok_2 = ok_2 and self.field.field[i][2 - i]
        if ok_1 or ok_2:
            return True
        return False