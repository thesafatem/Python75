class Checker:
    def __init__(self, field):
        self.field = field
        self.in_a_row = min(self.field.size, 5)

    def check(self, player):
        for i in range(self.field.size):
            for j in range(self.field.size - self.in_a_row + 1):
                ok_row = True
                ok_col = True
                for k in range(self.in_a_row):
                    ok_row = ok_row and self.field.field[i][j + k] == player.symbol
                    ok_col = ok_col and self.field.field[j + k][i] == player.symbol
                if ok_row or ok_col:
                    return True
        for i in range(self.field.size):
            for j in range(self.field.size - self.in_a_row + 1):
                if i >= self.in_a_row - 1:
                    ok = True
                    for k in range(self.in_a_row):
                        ok = ok and self.field.field[i - k][j + k] == player.symbol
                    if ok:
                        return True
                if i <= self.field.size - self.in_a_row:
                    ok = True
                    for k in range(self.in_a_row):
                        ok = ok and self.field.field[i + k][j + k] == player.symbol
                    if ok:
                        return True
        return False
