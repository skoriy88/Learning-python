#!/usr/local/bin/python
"""
Выгружает произвольный файл по FTP в двоичном режиме.
Использует анонимный доступ к ftp, если функции не был передан
кортеж user=(имя, пароль) аргументов.
"""

import ftplib
def putfile(file, site, dir, user=(), *, verbose=True):
    """
    uploads file in binary mode using
    FTP into site with anonymous access
    """
    if verbose: print('Uploading', file)
    local = open(file, 'rb')
    remote = ftplib.FTP(site)
    remote.login(*user)
    remote.cwd(dir)
    remote.storbinary('STOR' + file, local, 1024)
    remote.quit()
    local.close()
    if verbose: print('Upload done.')

if __name__ =='__main__':
    site = 'ftp.rmi.net'
    dir = '.'
    import sys, getpass
    pwd = getpass.getpass(site+' pwd?')
    putfile(sys.argv[1], site, dir, user=('lutz', pwd))
