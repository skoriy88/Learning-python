"""
############################################################################
тестирование режимов socket_stream_redirection.py
############################################################################
"""
import sys, os, multiprocessing
from socket_stream_redirect import *

############################################################################
# перенаправление вывода в клиенте
############################################################################

def server1():
    mypid = os.getpid()
    conn = initListenerSocket()         # блокируется до подключения клиента
    file = conn.makefile('r')
    for i in range(3):                  # читать вывод клиента
        data = file.readline().rstrip() # блокируется до поступления данных
        print('server %s got [%s]' % (mypid, data)) # вывод в окно терминала

def client1():
    mypid = os.getpid()
    redirectOut()
    for i in range(3):
        print('client %s: %s' % (mypid, i))  # вывод в сокет
        sys.stdout.flush()                   # иначе останется в буфере
                                             # до завершения!

############################################################################
# перенаправление ввода в клиенте
############################################################################

def server2():
    mypid = os.getpid()          # простой сокет без буферизации
    conn = initListenerSocket()  # отправляет в поток ввода клиента
    for i in range(3):
        conn.send(('server %s: %s\n' % (mypid, i)).encode())

def client2():
    mypid = os.getpid()
    redirectIn()
    for i in range(3):
        data = input()                              # ввод из сокета
        print('client %s got [%s]' % (mypid, data)) # вывод в окно терминала

############################################################################
# перенаправление ввода и вывода в клиенте, клиент является
# клиентом для сокета
############################################################################

def server3():
    mypid = os.getpid()
    conn = initListenerSocket()  # ждать подключения клиента
    file = conn.makefile('r')    # принимает от print(), передает в input()
    for i in range(3):           # readline блокируется до появления данных
        data = file.readline().rstrip()
        conn.send(('server %s got [%s]\n' % (mypid, data)).encode())

def client3():
    mypid = os.getpid()
    redirectBothAsClient()
    for i in range(3):
        print('client %s: %s' % (mypid, i))  # вывод в сокет
        data = input()  # ввод из сокета: выталкивает!
        sys.stderr.write('client %s got [%s]\n' % (mypid, data))  # не был
        # перенаправлен

############################################################################
# перенаправление ввода и вывода в клиенте, клиент является
# сервером для сокета
############################################################################

def server4():
    mypid = os.getpid()
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    file = sock.makefile('r')
    for i in range(3):
        sock.send(('server %s: %s\n' % (mypid, i)).encode())  # передать
        # в input()
        data = file.readline().rstrip()  # принять от print()
        print('server %s got [%s]' % (mypid, data))  # результат в терминал

def client4():
    mypid = os.getpid()
    redirectBothAsServer()  # играет роль сервера в этом режиме
    for i in range(3):
        data = input()  # ввод из сокета: выталкивает выходной буфер!
        print('client %s got [%s]' % (mypid, data))  # вывод в сокет
        sys.stdout.flush()  # иначе последняя порция данных останется
        # в буфере до завершения!

############################################################################
# перенаправление ввода и вывода в клиенте, клиент является клиентом
# для сокета, сервер первым инициирует обмен
############################################################################

def server5():
    mypid = os.getpid()  # тест № 4, но соединение принимает сервер
    conn = initListenerSocket()  # ждать подключения клиента
    file = conn.makefile('r')  # принимает от print(), передает в input()
    for i in range(3):
        conn.send(('server %s: %s\n' % (mypid, i)).encode())
        data = file.readline().rstrip()
        print('server %s got [%s]' % (mypid, data))

def client5():
    mypid = os.getpid()
    s = redirectBothAsClient() # играет роль клиента в этом режиме
    for i in range(3):
        data = input()         # ввод из сокета: выталкивает выходной буфер!
        print('client %s got [%s]' % (mypid, data))  # вывод в сокет
        sys.stdout.flush()     # иначе последняя порция данных останется
                               # в буфере до завершения!

############################################################################
# номер выполняемого теста определяется аргументом командной строки
############################################################################

if __name__ == '__main__':
    server = eval('server' + sys.argv[1])
    client = eval('client' + sys.argv[1])  # клиент – в этом процессе
    multiprocessing.Process(target=server).start()  # сервер –
                                                    # в новом процессе
    client()                               # переустановить потоки в клиенте
    #import time; time.sleep(5)            # проверка эффекта выталкивания
                                           # буферов при выходе

