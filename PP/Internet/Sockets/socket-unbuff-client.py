import time      # отправляет три сообщения через файл­обертку и сокет
from socket import *
sock = socket()  # по умолчанию=AF_INET, SOCK_STREAM (tcp/ip)
sock.connect(('localhost', 60000))
file = sock.makefile('w', buffering=1)  # по умолчанию=полная буферизация,
                                        # 0=ошибка, 1 не включает построчную
                                        # буферизацию!
print('sending data1')
file.write('spam\n')
time.sleep(5)  # следующий вызов flush() должен вызвать немедленную передачу
#file.flush()  # раскомментируйте вызовы flush(), чтобы увидеть разницу
print('sending data2')     # дополнительный вывод в файл не приводит
print('eggs', file=file)   # к выталкиванию буфера
time.sleep(5) # вывод будет принят сервером только после выталкивания буфера
#file.flush() # или после завершения
print('sending data3')     # низкоуровневый двоичный интерфейс выполняетпередачу
sock.send(b'ham\n')   # немедленно, эта строка будет принята первой, если
time.sleep(5)         # в первых двух случаях не выталкивать буферы вручную!
