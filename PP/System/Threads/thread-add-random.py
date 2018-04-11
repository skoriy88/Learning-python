"выводит различные результаты при каждом запуске под Windows 7"
import threading, time
count = 0
def adder():
    global count
    count = count + 1  # изменяет глобальную переменную
    time.sleep(0.5)    # потоки выполнения совместно используют
    count = count + 1  # глобальные объекты и переменные
threads = []
for i in range(100):
    thread = threading.Thread(target=adder, args=())
    thread.start()
    threads.append(thread)
for thread in threads: thread.join()
print(count)
