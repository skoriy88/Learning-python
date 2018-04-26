#!/usr/local/bin/python
"""
Сценарий на языке Python для загрузки медиафайла по FTP и его проигрывания.
Использует getfile.py, вспомогательный модуль, инкапсулирующий
этап загрузки по FTP.
"""
import getfile
from getpass import getpass
filename = 'monkeys.jpg'
# получить файл с помощью вспомогательного модуля
getfile.getfile(file=filename,
                site='ftp.rmi.net',
                dir ='.',
                user=('lutz', getpass('Pswd?')),
                refetch=True)
# остальная часть сценария осталась без изменений
if input('Open file?') in ['Y', 'y']:
    from PP.System.Media.playfile import playfile
    playfile(filename)
