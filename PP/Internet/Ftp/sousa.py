#!/usr/local/bin/python
"""
Порядок использования: sousa.py. Загружает и проигрывает музыкальную
тему Monty Python. В текущем виде может не работать в вашей системе:
он требует, чтобы компьютер был подключен к Интернету, имелась
учетная запись на сервере FTP, и использует аудиофильтры в Unix и плеер
файлов .au в Windows. Настройте этот файл и файл playfile.py, как требуется.
"""

from getpass import getpass
from Internet.Ftp.getfile import getfile
from System.Media.playfile import playfile

file = 'sousa.au'
site = 'ftp.rmi.net'
dir = '.'
user = ('lutz', getpass('Pwd?'))

getfile(file, site, dir, user)
playfile(file)

import os
os.system('getone.py sousa.au')