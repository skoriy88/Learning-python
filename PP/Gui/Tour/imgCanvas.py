gifdir = "D:/Projects/python/Gifs/"
from PIL.ImageTk import PhotoImage
from tkinter import *
win = Tk()
img = PhotoImage(file=gifdir + "1.gif")
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2, image=img, anchor=NW)   # координаты x, y
win.mainloop()
