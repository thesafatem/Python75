import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame()
frame2 = tk.Frame()

label_red = tk.Label(
    master=frame1,
    bg='red',
    width=50,
    height=20
).pack()
label_yellow = tk.Label(
    master=frame2,
    bg='yellow',
    width=50,
    height=20
).grid(row=0, column=0)
label_green = tk.Label(
    master=frame2,
    bg='green',
    width=50,
    height=20
).grid(row=0, column=1)

frame1.pack()
frame2.pack()

# label_yellow = tk.Label(
#     bg='yellow',
#     width=50,
#     height=20
# ).grid(row=0, column=0)
# label_green = tk.Label(
#     bg='green',
#     width=50,
#     height=20
# ).grid(row=0, column=1)
# label_red = tk.Label(
#     bg='red',
#     width=50,
#     height=20
# ).pack()

root.mainloop()