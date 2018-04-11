'''
Отыскивает наибольший файл с исходным программным кодом на языке Python
в единственном каталоге.
Поиск выполняется в каталоге стандартной библ иотеки Python для Windows, если
в аргументе командной строки не был указан какой-то другой каталог.
'''
import os, glob, sys, pprint
dirname = r'C:\Users\USER\AppData\Local\Programs\Python\Python36-32\Lib' if len(sys.argv) == 1 else sys.argv[1]
allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])