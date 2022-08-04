import tkinter
from tkinter import *
gui = Tk()
gui.title("todo")


with open("data.txt", 'r') as f:
    Label(gui, text=f.read()).pack()

gui.mainloop()
