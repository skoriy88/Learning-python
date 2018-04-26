#!/usr/local/bin/python
"""
Загружает произвольный файл по FTP. Используется анонимный доступ к FTP,
если не указан кортеж user=(имя, пароль). В разделе самопроверки
используются тестовый FTP­сайт и файл.
"""

from ftplib import FTP
from os.path import exists

def getfile(file, site, dir, user=(), *, verbose=True, refetch=False):
    '''
    Downloads a file in binary mode using FTP from site/dir
    with anonymous access or exists account
    '''
    if exists(file) and not refetch:
        if verbose: print(file, 'already fetched')
    else:
        if verbose: print('Downloading', file)
        local = open(file, 'wb')
        try:
            remote = FTP(site)
            remote.login(*user)
            remote.cwd(dir)
            remote.retrbinary('RETR ' + file, local.write, 1024)
            remote.quit()
        finally:
            local.close()
        if verbose: print('Download done.')

if __name__ == '__main__':
    from getpass import getpass
    file = 'monkeys.jpg'
    dir = '.'
    site = 'ftp.rmi.net'
    user = ('lutz', getpass('Pwd?'))
    getfile(file, site, dir, user)
