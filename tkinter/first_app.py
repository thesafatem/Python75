import tkinter as tk
import tkinter.font as tkFont
root = tk.Tk()


def int_to_hexadecimal(x):
    d = {"10": "A", "11": "B", "12": "C",
         "13": "D", "14": "E", "15": "F"}
    b = str(x % 16)
    if len(b) == 2:
        b = d[b]
    a = str(x // 16)
    if len(a) == 2:
        a = d[a]
    return a + b


def rgb_to_hexadecimal(red, green, blue):
    res = "#" + int_to_hexadecimal(red) + \
            int_to_hexadecimal(green) + \
            int_to_hexadecimal(blue)
    return res


# new_font = tkFont.Font(family="Lucida Grande", size=20)

label = tk.Label(
    text='Hello, world',
    width=30,
    height=12,
    background='red',
    foreground='white',
    # font=new_font
)
label.pack()

entry = tk.Entry(
    width=50,
    bg='green',
    fg='yellow'
)
entry.pack()

text = tk.Text(
    width=30,
    height=3,
    bg=rgb_to_hexadecimal(150, 150, 150)
).pack()


button = tk.Button(
    text='Push me',
    bg=rgb_to_hexadecimal(30, 113, 81),
    width=20,
    height=5,
    command=lambda: label.configure(bg="black") if label.cget("bg") == 'red' else label.configure(bg="red")
).pack()


def change_text():
    text = entry.get()
    label.configure(text=text)


def create_label():
    tk.Label(
        width=10,
        height=4,
        bg=rgb_to_hexadecimal(240, 240, 240),
        text='Hello'
    ).pack()


button2 = tk.Button(
    text='And then just touch me',
    bg=rgb_to_hexadecimal(30, 113, 81),
    width=20,
    height=5,
    command=create_label
).pack()

root.mainloop()























