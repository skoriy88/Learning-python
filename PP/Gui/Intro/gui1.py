from tkinter import *                           # импортировать виджет
widget = Label(None, text='Hello GUI world!')   # создать его
widget.pack(expand=YES, fill=BOTH)              # разместить
widget.mainloop()                               # запустить цикл событий