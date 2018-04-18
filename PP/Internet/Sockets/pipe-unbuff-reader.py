# вывод появится только через 10 секунд, если не использовать флаг Python ­u
# или sys.stdout.flush(); однако вывод будет появляться каждые 2 секунды,
# если использовать любой из этих двух вариантов
import os                                                # итератор читает
for line in os.popen('python -u pipe-unbuff-writer.py'): # строки
    print(line, end='')