from random import shuffle
import tkinter as tk
import time

root = tk.Tk()

colors = ['red', 'green', 'blue', 'skyblue',
          'yellow', 'brown', 'violet', 'orange']

colors = colors + colors

shuffle(colors)

colors = [colors[i:i+4] for i in [0, 4, 8, 12]]

last_tile = None

tiles = [[None for i in range(4)] for j in range(4)]

def change_color(self):
    if self.cget('bg') == 'grey':
        self.configure(bg=self.main_color)
    else:
        self.configure(bg='grey')


def f(self):
    global last_tile
    change_color(self)
    if last_tile is not None:
        if tiles[last_tile[0]][last_tile[1]].main_color == self.main_color:
            self["state"] = "disabled"
            tiles[last_tile[0]][last_tile[1]]["state"] = "disabled"
            last_tile = None
        else:
            change_color(tiles[last_tile[0]][last_tile[1]])
            change_color(self)
            # last_tile = (self.row, self.column)
            last_tile = None
    else:
        last_tile = (self.row, self.column)
    print(last_tile)


class Tile(tk.Button):
    def __init__(self, main_color, i, j, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.main_color = main_color
        self.row = i
        self.column = j
        self.configure(
            bg='grey',
            width=25,
            height=10,
            command=lambda: f(self)
        )


for i in range(4):
    for j in range(4):
        tiles[i][j] = Tile(colors[i][j], i, j)
        tiles[i][j].grid(row=i, column=j)


root.mainloop()