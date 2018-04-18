# вывод с построчной буферизацией (небуферизованный), когда stdout подключен
# к терминалу; при подключении к другим устройствам по умолчанию выполняется
# полная буферизация: используйте ­u или sys.stdout.flush(), чтобы избежать
# задержки вывода в канал/сокет
import time, sys
for i in range(5):             # режим буферизации потока влияет на print
    print(time.asctime())      # и на прямые операции доступа к файлу потока
    sys.stdout.write('spam\n') # если sys.stdout не был переустановлен
    time.sleep(2)              # в другой файл