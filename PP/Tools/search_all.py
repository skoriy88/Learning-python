'''
##############################################################################
Порядок использования: “python ...\Tools\search_all.py dir string”.
Отыскивает все файлы в указанном дереве каталогов, содержащие заданную строку;
для предварительного отбора имен файлов использует интерфейс os.walk вместо
find.find; вызывает visitfile для каждой строки в результатах, полученных
вызовом функции find.find с шаблоном “*”;
##############################################################################
'''

import os, sys
listonly = False
textexts = ['.py', '.pyw', '.txt', '.c', '.h']   # игнорировать двоичные файлы

def searcher(startdir, searchkey):
    global fcount, vcount
    fcount = vcount = 0
    for (thisDir, dirsHere, filesHere) in os.walk(startdir):
        for fname in filesHere:                  # для каждого некаталога
            fpath = os.path.join(thisDir, fname) # fname не содержит пути
            visitfile(fpath, searchkey)

def visitfile(fpath, searchkey):                 # для каждого некаталога
    global fcount, vcount                        # искать строку
    print(vcount+1, '=>', fpath)                 # пропустить защищенные файлы
    try:
        if not listonly:
            if os.path.splitext(fpath)[1] not in textexts:
                print('Skipping', fpath)
            elif searchkey in open(fpath).read():
                input('%s has %s' % (fpath, searchkey))
                fcount += 1
    except:
        print('Failed:', fpath, sys.exc_info()[0])
    vcount += 1
if __name__ == '__main__':
    searcher(sys.argv[1], sys.argv[2])
    print('Found in %d files, visited %d' % (fcount, vcount))
