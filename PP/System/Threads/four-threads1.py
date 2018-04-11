import threading, _thread
def action(i):
    print(i ** 32)
# подкласс, хранящий собственную информацию о состоянии
class Mythread(threading.Thread):
    def __init__(self, i):
        self.i = i
        threading.Thread.__init__(self)
    def run(self):                       # переопределить метод run
        print(self.i ** 32)
Mythread(2).start()                      # метод start вызовет метод run()
# передача простой функции
thread = threading.Thread(target=(lambda: action(2)))     # run вызовет target
thread.start()
# то же самое, но без lambda-функции,
# сохраняющей информацию о состоянии в образуемом ею замыкании
threading.Thread(target=action, args=(2,)).start()      # вызываемый объект
                                                        # и его аргументы
# с помощью модуля thread
_thread.start_new_thread(action, (2,))        # полностью процедурный интерфейс
