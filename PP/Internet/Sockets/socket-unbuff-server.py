from socket import *       # читает три сообщения непосредственно из сокета
sock = socket()
sock.bind(('', 60000))
sock.listen(5)
print('accepting...')
conn, id = sock.accept()   # блокируется, пока не подключится клиент
for i in range(3):
    print('receiving...')
    msg = conn.recv(1024)  # блокируется, пока не поступят данные
    print(msg)             # выведет все строки сразу, если не выталкивать
                           # буфер вручную
