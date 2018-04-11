from tkinter import *                       # импортировать базовый набор виджетов,
from glob import glob                       # чтобы получить список файлов по расширению
import demoCheck                            # прикрепить демонстрационный пример с флажками
import random                               # выбрать случайную картинку
from PIL.ImageTk import PhotoImage
gifdir = 'D:/Projects/python/Gifs/'         # каталог по умолчанию с GIF-файлами

def draw():
    name, photo = random.choice(images)
    lbl.config(text=name)
    pix.config(image=photo)
root=Tk()
lbl = Label(root, text="none", bg='blue', fg='red')
pix = Button(root, text="Press me", command=draw, bg='white')
lbl.pack(fill=BOTH)
pix.pack(pady=10)
demoCheck.Demo(root, relief=SUNKEN, bd=2).pack(fill=BOTH)
files = glob(gifdir + "*")                    # имеющиеся GIF-файлы
images = [(x, PhotoImage(file=x)) for x in files] # загрузить и сохранить
print(files)
root.mainloop()
