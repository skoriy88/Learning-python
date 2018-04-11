import threading, _thread

# обычный класс с атрибутами, ООП
class Power:
    def __init__(self, i):
        self.i = i
    def action(self):
        print(self.i ** 32)
obj = Power(2)
threading.Thread(target=obj.action).start()    # запуск связанного метода
# вложенная область видимости, для сохранения информации о состоянии
def action(i):
    def power():
        print(i ** 32)
    return power
threading.Thread(target=action(2)).start()     # запуск возвращаемой функции
# запуск обоих вариантов с помощью модуля _thread
_thread.start_new_thread(obj.action, ())       # запуск вызываемого объекта
_thread.start_new_thread(action(2), ())
