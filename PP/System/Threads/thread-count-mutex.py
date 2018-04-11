'''
синхронизирует доступ к stdout: так как это общий глобальный объект, данные,
которые выводятся из потоков выполнения, могут перемешиваться, если  не
синхронизировать операции
'''
import _thread as thread, time
def counter(myId, count):                  # эта функция выполняется в потоках
    for i in range(count):
        time.sleep(1)                        # имитировать работу
        mutex.acquire()
        print('[%s] => %s' % (myId, i))      # теперь работа функции print
                                             # не будет прерываться
        mutex.release()
mutex = thread.allocate_lock()               # создать объект блокировки
for i in range(5):                           # породить 5 потоков выполнения
    thread.start_new_thread(counter, (i, 5)) # каждый поток выполняет 5 циклов
time.sleep(6)
print('Main thread exiting.')                # задержать выход из программы