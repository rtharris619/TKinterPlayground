import tkinter as tk

window = tk.Tk()


def add_label():
    greeting = tk.Label(text="Hello, tkinter", fg="white", bg="black", width=10, height=20)
    greeting.pack()


def add_button():
    button = tk.Button(text="Click me", width=25, height=5, bg="blue", fg="yellow")
    button.pack()


def add_user_input():
    label = tk.Label(text="Name")
    entry = tk.Entry()
    label.pack()
    entry.pack()


def add_frame():
    frame_a = tk.Frame()
    frame_b = tk.Frame()

    label_a = tk.Label(master=frame_a, text="Frame a")
    label_a.pack()

    label_b = tk.Label(master=frame_b, text="Frame b")
    label_b.pack()

    frame_a.pack()
    frame_b.pack()


def add_frame_with_reliefs():
    border_effects = {
        "flat": tk.FLAT,
        "sunken": tk.SUNKEN,
        "raised": tk.RAISED,
        "groove": tk.GROOVE,
        "ridge": tk.RIDGE,
    }

    for relief_name, relief in border_effects.items():
        frame = tk.Frame(master=window, relief=relief, borderwidth=5)
        frame.pack(side=tk.LEFT)
        label = tk.Label(master=frame, text=relief_name)
        label.pack()


def pack_example():
    frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
    frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
    frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")

    frame1.pack()
    frame2.pack()
    frame3.pack()


def pack_with_fill():
    frame1 = tk.Frame(master=window, height=100, bg="red")
    frame2 = tk.Frame(master=window, height=50, bg="yellow")
    frame3 = tk.Frame(master=window, height=25, bg="blue")

    frame1.pack(fill=tk.X)
    frame2.pack(fill=tk.X)
    frame3.pack(fill=tk.X)


def pack_with_side():
    frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
    frame2 = tk.Frame(master=window, width=100, height=50, bg="yellow")
    frame3 = tk.Frame(master=window, width=50, height=25, bg="blue")

    frame1.pack(fill=tk.Y, side=tk.LEFT)
    frame2.pack(fill=tk.Y, side=tk.LEFT)
    frame3.pack(fill=tk.Y, side=tk.LEFT)


def pack_with_expand():
    frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
    frame2 = tk.Frame(master=window, width=100, bg="yellow")
    frame3 = tk.Frame(master=window, width=50, bg="blue")

    frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


def place_example():
    frame = tk.Frame(master=window, width=150, height=150)
    frame.pack()

    label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
    label1.place(x=0, y=0)

    label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
    label2.place(x=75, y=75)


def grid_example():
    for i in range(3):
        for j in range(3):
            frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
            label.pack()


grid_example()

window.mainloop()
