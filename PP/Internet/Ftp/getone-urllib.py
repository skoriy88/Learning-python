#!/usr/local/bin/python
"""
Сценарий на языке Python для загрузки файла по строке адреса URL;
вместо ftplib использует более высокоуровневый модуль urllib;
urllib поддерживает протоколы FTP, HTTP, HTTPS на стороне клиента,
локальные файлы, может работать с прокси­серверами, выполнять инструкции
перенаправления, принимать cookies и многое другое; urllib также
позволяет загружать страницы html, изображения, текст и так далее;
смотрите также парсеры Python разметки html/xml веб­страниц,
получаемых с помощью urllib, в главе 19;
"""

import os, getpass
from urllib.request import urlopen

filename = 'monkeys.jpg'
password = getpass.getpass('Pwd?')

remoteaddr = 'ftp://lutz:%s@ftp.rmi.net/$s; type=i' % (password, filename)
print('Downloading', remoteaddr)

#urllib.request.urlretrieve(remoteaddr, filename)

remotefile = urlopen(remoteaddr)
localfile = open(filename, 'wb')
localfile.write(remotefile.read())
localfile.close()
remotefile.close()
