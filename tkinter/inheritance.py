import tkinter as tk

root = tk.Tk()


class NewButton(tk.Button):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.configure(command=lambda: self.configure(bg='white') if self.cget('bg') != 'white' else self.configure(bg=kw['bg']))


class NewFrame(tk.Frame):
    def __init__(self, _width, _height, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.label1 = tk.Label(
            master=self,
            bg='red',
            width= _width // 2,
            height= _height // 2
        ).grid(row=0, column=0)
        self.label2 = tk.Label(
            master=self,
            bg='green',
            width=_width // 2,
            height=_height // 2
        ).grid(row=1, column=0)
        self.label3 = tk.Label(
            master=self,
            bg='blue',
            width=_width // 2,
            height=_height // 2
        ).grid(row=1, column=1)


frame = NewFrame(100, 40)
frame.pack()

frame2 = NewFrame(50, 20, master=frame)
frame2.grid(row=0, column=1)

frame3 = NewFrame(25, 10, master=frame2)
frame3.grid(row=0, column=1)


# button = NewButton(
#     master=root,
#     bg='red',
#     text='Hello',
#     width=25,
#     height=10
# )
#
# button.pack()

# button.configure(fg='white')



root.mainloop()