import tkinter 
from tkinter import *
import runpy

gui = Tk()

def write():
    runpy.run_path(path_name='todo.py')


def read():
    exec(open(r'reader.py').read())

button1 =  Button(gui, text="Write to File", command=write)
button1.pack(side=tkinter.LEFT)

button2 = Button(gui, text = "Read File", command=read)
button2.pack(side=tkinter.RIGHT)

gui.mainloop()
