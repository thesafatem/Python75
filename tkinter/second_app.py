import tkinter as tk

root = tk.Tk()

label_red = tk.Label(
    bg='red',
    width=25,
    height=20,
    align='right'
).grid(row=0, column=0)
label_red = tk.Label(
    bg='red',
    width=25,
    height=20,
    align='left'
).grid(row=0, column=1)
label_yellow = tk.Label(
    bg='yellow',
    width=50,
    height=20
).grid(row=1, column=0)
label_green = tk.Label(
    bg='green',
    width=50,
    height=20
).grid(row=1, column=1)
# label_blue = tk.Label(
#     bg='blue',
#     width=50,
#     height=20
# ).grid(row=10, column=10)



root.mainloop()