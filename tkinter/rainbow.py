import tkinter as tk

root = tk.Tk()

# red = tk.Label(
#     bg='red',
#     width=20,
#     height=8,
#     text='Каждый'
# ).grid(row=0, column=0)
# orange = tk.Label(
#     bg='orange',
#     width=20,
#     height=8,
#     text='охотник'
# ).grid(row=0, column=1)
# yellow = tk.Label(
#     bg='yellow',
#     width=20,
#     height=8,
#     text='желает'
# ).grid(row=0, column=2)
# green = tk.Label(
#     bg='green',
#     width=20,
#     height=8,
#     text='знать'
# ).grid(row=0, column=3)
# skyblue = tk.Label(
#     bg='skyblue',
#     width=20,
#     height=8,
#     text='где'
# ).grid(row=0, column=4)
# blue = tk.Label(
#     bg='blue',
#     width=20,
#     height=8,
#     text='сидит'
# ).grid(row=0, column=5)
# violet = tk.Label(
#     bg='violet',
#     width=20,
#     height=8,
#     text='фазан'
# ).grid(row=0, column=6)

w = 'Каждый, охотник, желает, знать, где, сидит, фазан'
words = w.split(', ')
c = 'red, orange, yellow, green, skyblue, blue, violet'
colors = c.split(', ')

label = tk.Label(
    height=8,
    width=20
)

for i in range(7):
    tk.Button(
        width=20,
        height=8,
        text=words[i],
        bg=colors[i],
        command=lambda j=i: label.configure(text=words[j])
    ).grid(row=0, column=i)

label.grid(row=1, column=3)

root.mainloop()