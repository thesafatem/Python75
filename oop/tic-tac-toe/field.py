class Field:
    def __init__(self, size):
        self.size = size
        self.field = [[' ' for i in range(self.size)] for j in range(self.size)]

    def __str__(self):
        res = " "
        for j in range(self.size):
            res += f"   {j}"
        res += "\n\n"
        for i in range(self.size):
            res += f"{i}   {self.field[i][0]} "
            for j in range(1, self.size):
                res += f"| {self.field[i][j]} "
            res += "\n"
            if i != self.size - 1:
                res += ' ' * 3 + '-' * (4 * self.size - 1) + '\n'
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