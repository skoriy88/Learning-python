#!/bin/env python
"""
############################################################################
использует протокол FTP для копирования (загрузки) всех файлов
из единственного каталога на удаленном сайте в каталог на локальном
компьютере; запускайте этот сценарий периодически для создания зеркала
плоского каталога FTP­сайта, находящегося на сервере вашего провайдера;
для анонимного доступа установите переменную remoteuser в значение
'anonymous'; чтобы пропускать ошибки загрузки файлов, можно было бы
использовать инструкцию try, но в случае таких ошибок FTP­соединение скорее
всего все равно будет закрыто автоматически; можно было бы перед передачей
каждого нового файла переустанавливать соединение, создавая новый экземпляр
класса FTP: сейчас устанавливается всего одно соединение; в случае неудачи
попробуйте записать в переменную nonpassive значение True, чтобы
использовать активный режим FTP, или отключите брандмауэр; кроме того,
работоспособность этого сценария зависит от настроек сервера FTP
и возможных ограничений на загрузку.
############################################################################
"""

import os, sys, ftplib
from getpass import getpass
from mimetypes import guess_type

nonpassive = False
remotesite = 'home.rmi.net'
remotedir = '.'
remoteuser = 'lutz'
remotepass = getpass('Password for %s on %s: ' % (remoteuser, remotesite))
localdir = (len(sys.argv) > 1 and sys.argv[1]) or '.'
cleanall = input('Clean local directory first? ')[:1] in ['y', 'Y']

'''
nonpassive = False
remotesite = input("Enter ftp-address: ")
remotedir = input("Enter ftp-dir: ")
remoteuser = input('Enter username: ')
remotepass = getpass('Password for %s on %s: ' % (remoteuser, remotesite))
localdir = (len(sys.argv) > 1 and sys.argv[1]) or '.'
cleanall = input('Clean local directory first? ')[:1] in ['y', 'Y']
'''

print('connecting...')
connection = ftplib.FTP(remotesite)
connection.login(remoteuser, remotepass)
connection.cwd(remotedir)
if nonpassive:
    connection.set_pasv(False)

if cleanall:
    for localname in os.listdir(localdir):
        try:
            print('deleting ,local', localname)
            os.remove(os.path.join(localdir, localname))
        except:
            print('cannot delete local', localname)

count = 0
remotefiles = connection.nlst()

for remotename in remotefiles:
    if remotename in ('.', '..'): continue
    mimetype, encoding = guess_type(remotename)
    mimetype = mimetype or '?/?'
    maintype = mimetype.split('/')[0]
    localpath = os.path.join(localdir, remotename)
    print('downloading', remotename, 'to', localpath, end=' ')
    print('as', maintype, encoding or '')

    if maintype == 'text' and encoding == None:
        localfile = open(localpath, 'w', encoding=connection.encoding)
        callback = lambda line: localfile.write(line + '\n')
        connection.retrlines('RETR ' + remotename, callback)
    else:
        localfile = open(localpath, 'wb')
        connection.retrbinary('RETR ' + remotename, localfile.write)

    localfile.close()
    count += 1

connection.quit()
print('Done: ', count, 'files downloaded.')
