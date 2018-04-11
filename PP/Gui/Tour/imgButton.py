gifdir = "D:/Projects/python/Gifs//"
from tkinter import *
win = Tk()
img = PhotoImage(file=gifdir + "2.gif")
Button(win, image=img).pack()
win.mainloop()
