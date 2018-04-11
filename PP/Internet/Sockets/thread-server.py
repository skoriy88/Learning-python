"""
At the servers side: open socket with entered number of port,
waiting for message from client and send it beck to him,
continues to send message? until the eof-mark would be get,
from client side; for client handling generates the child execution threads,
which uses global memory together with main thread;
can work both on Unix and Win
"""

import time, _thread as thread # или использовать threading.Thread().start()
from socket import *        # получить конструктор сокетов и константы
myHost = ''                 # компьютер­сервер, '' означает локальный хост
myPort = 50007              # использовать незарезервированный номер порта

sockobj = socket(AF_INET, SOCK_STREAM)  # создать объект сокета TCP
sockobj.bind((myHost, myPort))          # связать с номером порта сервера
sockobj.listen(5)                       # не более 5 ожидающих запросов

def now():
    return time.ctime(time.time())      # текущее время на сервере

def handleClient(connection):           # в дочернем потоке: ответить
    time.sleep(5)                       # имитировать блокирующие действия
    while True:                         # чтение, запись в сокет клиента
        data = connection.recv(1024)
        if not data: break
        reply = 'Echo=>%s at %s' % (data, now())
        connection.send(reply.encode())
    connection.close()

def dispatcher():                       # пока процесс работает,
    while True:                         # ждать запроса очередного клиента,
        connection, address = sockobj.accept()         # передать потоку
        print('Server connected by', address, end=' ') # для обслуживания
        print('at', now())
        thread.start_new_thread(handleClient, (connection,))

dispatcher()
