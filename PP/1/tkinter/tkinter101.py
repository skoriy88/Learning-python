from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='Проба', message='Кнопка нажата!')

window = Tk()
button = Button(window, text='Нажми', command=reply)
button.pack()
window.mainloop()