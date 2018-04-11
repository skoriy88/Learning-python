'''
то же, что и предыдущий пример, но выводит значения, возвращаемые диалогами;
lambda-выражение сохраняет данные из локальной области видимости для передачи их
обработчику (обработчик события нажатия кнопки обычно не получает аргументов,
а автоматические ссылки в объемлющую область видимости некорректно работают
с переменными цикла) и действует подобно вложенной инструкции def, такой как:
def func(key=key): self.printit(key)
'''
from tkinter import *                  # импортировать базовый набор виджетов
from dialogTable import demos          # обработчики событий от кнопок
from quitter import Quitter            # прикрепить к себе объект quit
class Demo(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text="Дэмо-примеры").pack()
        for key in demos:
            func = (lambda key=key: self.printit(key))
            Button(self, text=key, command=func).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)
    def printit(self, name):
        print(name, 'возвращает =>', demos[name]()) # извлечь, вызвать, вывести
if __name__ == '__main__': Demo().mainloop()
