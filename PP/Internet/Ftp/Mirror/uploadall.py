#!/bin/env python
"""
############################################################################
расширяет класс FtpTools, обеспечивая возможность выгрузки всех файлов
и подкаталогов из локального дерева каталогов в удаленный каталог
на сервере; поддерживает вложенные подкаталоги, но не поддерживает
операцию cleanall (для этого необходимо анализировать листинги FTP,
чтобы определять удаленные каталоги: смотрите сценарий cleanall.py);
для выгрузки подкаталогов используется os.path.isdir(path),
которая проверяет, является ли в действительности локальный файл каталогом,
метод FTP().mkd(path) ­ для создания каталогов на сервере (вызов обернут
инструкцией try, на случай если каталог уже существует на сервере),
и рекурсия – для выгрузки всех файлов/каталогов внутри
вложенного подкаталога.
############################################################################
"""

import os, ftptools

class UploadAll(ftptools.FtpTools):
    '''
    uploads whole dir tree, expects the main dir already exists
    '''
    def __init__(self):
        self.fcount = self.dcount = 0


    def getcleanall(self):
        return False

    def uploadDir(self, localdir):
        '''
        uploads files for every dir, makes recursive call for subdirs
        '''
        #self.connection.mkd(remotedir)
        #self.connection.cwd(remotedir)
        localfiles = os.listdir(localdir)
        for localname in localfiles:
            localpath = os.path.join(localdir, localname)
            print('uploading', localpath, 'to', localname, end = ' ')
            if not os.path.isdir(localpath):
                self.uploadOne(localname, localpath, localname)
                self.fcount += 1
            else:
                try:
                    self.connection.mkd(localname)
                    print('directory created')
                except:
                    print('directory not created')
                self.connection.cwd(localname)
                self.uploadDir(localpath)
                self.connection.cwd('..')
                self.dcount += 1
                print('directory exited')

if __name__ == '__main__':
    ftp = UploadAll()
    ftp.configTransfer()
    ftp.run(transferAct = lambda: ftp.uploadDir(ftp.localdir))
    print('Done: ', ftp.fcount, 'files and',
          ftp.dcount, 'directories uploaded.')


