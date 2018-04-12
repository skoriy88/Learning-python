"""
проверка эффекта связывания стандартных потоков ввода­вывода с файлами,
открытыми в текстовом и двоичном режимах; то же справедливо и для socket.
makefile: функция print требует текстовый режим, а текстовый режим,
в свою очередь, препятствует отключению буферизации –
используйте ключ ­u или вызывайте метод sys.stdout.flush()
"""
import sys
def reader(F):
    tmp, sys.stdin = sys.stdin, F
    line = input()
    print(line)
    sys.stdin = tmp
reader(open('test­stream­modes.py'))        # работает: input() возвращает
                                            # текст
reader(open('test­stream­modes.py', 'rb'))  # работает: но input()
                                            # возвращает байты
def writer(F):
    tmp, sys.stdout = sys.stdout, F
    print(99, 'spam')
    sys.stdout = tmp
writer( open('temp', 'w') )     # работает: print() передает .write()
                                # текст str
print( open('temp').read() )
writer( open('temp', 'wb') )    # ОШИБКА в print: двоичный режим
                                # требует байты
writer( open('temp', 'w', 0) )  # ОШИБКА в open: буферизация в текстовом
                                # режиме обязательна
