class Field:
    size = 3
    def __init__(self):
        self.field = [[' ' for i in range(self.size)] for j in range(self.size)]

    def __str__(self):
        res = ""
        res += '    0   1   2\n\n'
        for i in range(self.size):
            res += f"{i}   {self.field[i][0]} | {self.field[i][1]} | {self.field[i][2]}\n"
            if i != self.size - 1:
                res += ' ' * 3 + '-' * 11 + '\n'
        return res

    def fill(self, coords, symbol):
        # coords = (x, y)
        if coords[0] < 0 or coords[0] >= self.size \
            or coords[1] < 0 or coords[1] >= self.size:
            raise ValueError
        elif self.field[coords[0]][coords[1]] != ' ':
            raise ValueError
        else:
            self.field[coords[0]][coords[1]] = symbol