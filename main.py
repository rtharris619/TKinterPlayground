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


add_user_input()

window.mainloop()
