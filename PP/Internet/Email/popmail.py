#!/usr/local/bin/python

import poplib, getpass, sys
import mailconfig

mailserver = mailconfig.popservername
mailuser = mailconfig.popusername
mailpasswd = getpass.getpass('Password for %s?' % mailuser)

#print('Connecting...')
server = poplib.POP3(mailserver)
print(server)
server.user(mailserver)
server.pass_(mailpasswd)

try:
    print(server.getwelcome())
    msgCount, msgBytes = server.stat()
    print("there are", msgCount, 'mail messages in', msgBytes, 'bytes')
    print(server.list())
    print('-' * 80)
    input('[Press Enter key]')

    for i in range(msgCount):
        hdr, message, octets = server.retr(i+1)
        for line in message: print(line.decode())
        print('-' * 80)
        if i < msgCount -1:
            input('[Press Enter key]')
finally:
    server.quit()
print('Bye.')

