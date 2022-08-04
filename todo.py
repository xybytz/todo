import tkinter
from tkinter import *
gui = Tk()
gui.title("todo")
def writeFile():
    file = open('data.txt','a')
    file.write(metinF.get() + '\n')
    file.close()












metinF = Entry(gui)
metinF.grid(row=9, column=1)
ButtonWrite = Button(gui)
ButtonWrite = Button(gui)
ButtonWrite.config(text = 'Write To File', command = writeFile)
ButtonWrite.grid(row=8, column=1)
gui.mainloop()




