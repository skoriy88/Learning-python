#!/bin/env python
"""
############################################################################
использует протокол FTP для копирования (загрузки) всех файлов из каталога
на удаленном сайте в каталог на локальном компьютере; эта версия действует
точно так же, но была реорганизована с целью завернуть фрагменты
программного кода в функции, чтобы их можно было повторно использовать
в сценарии выгрузки каталога и, возможно, в других программах в будущем –
в противном случае избыточность программного кода может с течением времени
привести к появлению различий в изначально одинаковых фрагментах и усложнит
сопровождение.
############################################################################
"""

import os, sys, ftplib
from getpass import getpass
from mimetypes import guess_type, add_type

defaultSite = 'home.rmi.net'
defaultRdir = '.'
defaultUser = 'lutz'

def configTransfer(site=defaultSite, rdir=defaultRdir, user=defaultUser):
    class cf: pass
    cf.nonpassive = False
    cf.remotesite = site
    cf.remotedir = rdir
    cf.remoteuser = user
    cf.localdir = (len(sys.argv) > 1 and sys.argv[1]) or '.'
    cf.cleanall = input('Clean target directory first? ')[:1] in ['y', 'Y']
    cf.remotepass = getpass('Password for %s on %s:' % (cf.remoteuser, cf.remotesite))
    return cf

def isTextKind(remotename, trace=True):
    add_type('text/x­python­win', '.pyw')
    mimetype, encoding = guess_type(remotename, strict=False)
    mimetype = mimetype or '?/?'
    maintype = mimetype.split('/')[0]
    if trace: print(maintype, encoding or '')
    return maintype == 'text' and encoding == None

def connectFtp(cf):
    print('connecting...')
    connection = ftplib.FTP(cf.remotesite)
    connection.login(cf.remoteuser, cf.remotepass)
    connection.cwd(cf.remotedir)
    if cf.nonpassive:
        connection.set_pasv(False)
    return connection

def cleanLocals(cf):
    if cf.cleanall:
        for localname in os.listdir(cf.localdir):
            try:
                print('deleting local', localname)
                os.remove(os.path.join(cf.localdir, localname))
            except:
                print('cannot delete local', localname)

def downloadAll(cf, connection):
    remotefiles = connection.nlst()
    for remotename in remotefiles:
        if remotename in ('.', '..'): continue
        localpath = os.path.join(cf.localdir, remotename)
        print('downloading', remotename, 'to', localpath, 'as', end=' ')
        if isTextKind(remotename):
            localfile = open(localpath, 'w', encoding=connection.encoding)
            def callback(line): localfile.write(line + '\n')
            connection.retrlines('RETR ' + remotename, callback)
        else:
            localfile = open(localpath, 'wb')
            connection.retrbinary('RETR ' + remotename, localfile.write)
        localfile.close()
    connection.quit()
    print('Done:', len(remotefiles), 'files downloaded.')

if __name__ == '__main__':
    cf = configTransfer()
    conn = connectFtp(cf)
    cleanLocals(cf)
    downloadAll(cf, conn)

