#!/bin/env python
"""
############################################################################
расширяет класс FtpTools возможностью удаления файлов и подкаталогов
в дереве каталогов на сервере; поддерживает удаление вложенных подкаталогов;
зависит от формата вывода команды dir(), который может отличаться
на некоторых серверах! ­ смотрите подсказки в файле
Tools\Scripts\ftpmirror.py, в каталоге установки Python;
добавьте возможность загрузки дерева каталогов с сервера;
############################################################################
"""

from ftptools import FtpTools
class CleanAll(FtpTools):
    '''
    deletes all dir-tree on server
    '''
    def __init__(self):
        self.fcount = self.dcount = 0

    def getlocaldir(self):
        return None

    def getcleanall(self):
        return True

    def cleanDir(self):
        lines = []
        self.connection.dir(lines.append)

        for line in lines:
            parsed = line.split()
            permiss = parsed[0]
            fname = parsed[-1]
            if fname in ('.', '..'):
                continue
            elif permiss[0] != 'd':
                print('file', fname)
                self.connection.delete(fname)
                self.fcount += 1
            else:
                print('directory', fname)
                self.connection.cwd(fname)
                self.cleanDir()
                self.connection.cwd('..')
                self.connection.rmd(fname)
                self.dcount += 1
                print('directory exited')

if __name__ == '__main__':
    ftp = CleanAll()
    ftp.configTransfer()
    ftp.run(cleanTarget=ftp.cleanDir)
    print('Done:', ftp.fcount, 'files and', ftp.dcount,
          'directories cleaned.')