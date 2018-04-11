#!/usr/bin/python
'''
##############################################################################
разрезает файл на несколько частей; сценарий join.py объединяет эти части в один
файл; данный сценарий является настраиваемой версией стандартной команды split
в Unix; поскольку сценарий написан на языке Python, он с тем же успехом может
использоваться в Windows и легко может быть модифицирован; благодаря тому, что
он экспортирует функцию, его логику можно импортировать и повторно использовать
в других приложениях;
##############################################################################
'''
import sys, os
kilobytes = 1024
megabytes = kilobytes * 1000
chunksize = int(1.4 * megabytes)                    #по умолчанию: примерный размер

def split(fromfile, todir, chunksize=chunksize):
    if not os.path.exists(todir):                   #ошибки обрабатывает вызвавший
        os.mkdir(todir)                             #создать каталог для фрагментов
    else:
        for fname in os.listdir(todir):             #удалить все существующие файлы
            os.remove(os.path.join(todir, fname))
    partnum = 0
    input = open(fromfile, 'rb')                    # двоичный режим: без декодирования и без преобразования символов конца строки

    while True:                                     #eof = прочтена пустая строка
        chunk = input.read(chunksize)
        if not chunk: break
        partnum += 1
        filename = os.path.join(todir, ('part%04d' % partnum))
        fileobj = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()
    input.close()
    assert partnum <= 9999                          #сортировка в join невозможна, если будет 5 цифр
    return partnum

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: split.py [file-to-split target dir [chunksize]]')
    else:
        if len(sys.argv) < 3:
            interactive = True
            fromfile = input('File to be split?')    #ввод данных, если запущен щелчком мыши
            todir = input(('Directory to store part files?'))
        else:
            interactive = False
            fromfile, todir = sys.argv[1:3]          #аргументы командной строки
            if len(sys.argv) == 4: chunksize = int(sys.argv[3])
        absfrom, absto = map(os.path.abspath, [fromfile, todir])
        print('Splitting', absform, 'to', absto, 'by', chunksize)

        try:
            parts = split(fromfile, todir, chunksize)
        except:
            print('Error during split: ')
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print('Split finished: ', parts, 'parts are in ', absto)
        if interactive: input('Press Enter key')      #пауза, если сценарий запущен щелчком мыши




