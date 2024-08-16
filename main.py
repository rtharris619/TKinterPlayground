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


add_frame_with_reliefs()

window.mainloop()
