"""
4 демонстрационных класса, выполняемых как независимые процессы:
multiprocessing;
модуль multiprocessing позволяет запускать только именованные функции
с аргументами – он не может работать с lambda-выражениями, поскольку в Windows
они не могут быть сериализованы (глава 5); кроме того, модуль multiprocessing
имеет собственные инструменты взаимодействий между процессами, такие как каналы;
"""

from tkinter import *
from multiprocessing import Process
demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']

def runDemo(modname):              # запускается в новом процессе
    module = __import__(modname)   # создать GUI с нуля
    module.Demo().mainloop()

if __name__ == '__main__':
    for modname in demoModules:    # только в __main__!
        Process(target=runDemo, args=(modname,)).start()
    root = Tk()                    # граф. интерфейс родительского процесса
    root.title('Processes')
    Label(root, text='Multiple program demo: multiprocessing', 
                bg='white').pack()
    root.mainloop()