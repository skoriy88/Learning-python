#!/usr/local/bin/python
"""
Сценарий на языке Python для загрузки медиафайла по FTP и его проигрывания.
Использует модуль ftplib, реализующий поддержку протокола ftp на основе
сокетов. Протокол FTP использует 2 сокета (один для данных и один
для управления – на портах 20 и 21) и определяет форматы текстовых
сообщений, однако модуль ftplib скрывает большую часть деталей этого
протокола. Измените настройки в соответствии со своим сайтом/файлом.
"""

import os, sys
from getpass import getpass
from ftplib import FTP

nonpassive = False
filename = 'monkeys.jpg'
dirname = '.'
sitename = 'ftp.rmi.net'
userinfo = ('lutz', getpass('Pwd?'))    # () for anonimous
if len(sys.argv) > 1: filename = sys.argv[1]

print('Connecting...')
connection = FTP(sitename)
connection.login(*userinfo)
connection.cwd(dirname)
if nonpassive:
    connection.set_pasv(False)

print('Downloading...')
localfile = open(filename, 'wb')
connection.retrbinary('RETR ' + filename, localfile.write, 1024)
connection.quit()
localfile.close()

if input('Open file?') in ['Y', 'y']:
    from PP.System.Media.playfile import playfile
    playfile(filename)