gifdir = "D:/Projects/python/Gifs/"
from sys import argv
from tkinter import *
from PIL.ImageTk import PhotoImage
filename = argv[1] if len(argv) > 1 else '1.gif' # имя файла в командной строке?
win = Tk()
img = PhotoImage(file=gifdir + filename)
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height()) # размер соответственно
can.create_image(2, 2, image=img, anchor=NW)       # картинке
win.mainloop()