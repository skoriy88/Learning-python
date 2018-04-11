"""
отображает изображение с помощью альтернативного объекта из пакета PIL
поддерживает множество форматов изображений; предварительно установите пакет
PIL: поместите его в каталог Lib\site-packages
"""

import os, sys, random
from glob import glob  # чтобы получить список файлов по расширению
from tkinter import *
from PIL.ImageTk import PhotoImage # <== использовать альтернативный класс из
                                   # PIL, остальной программный код 
                                   # без изменений
imgdir = 'D:/Projects/python/Gifs/'
files = glob(imgdir + '*')
images = [x for x in files]
imgfile = random.choice(images)
if len(sys.argv) > 1:
    imgfile = sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)
win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath)  # теперь поддерживает и JPEG!
imgfile = random.choice(images)
Label(win, image=imgobj).pack()
win.mainloop()
print(imgobj.width(), imgobj.height()) # показать размер в пикселях при выходе