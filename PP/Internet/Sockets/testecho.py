import sys
from LUTZ.PP.launchmodes import QuietPortableLauncher

numclients = 8
def start(cmdline):
    QuietPortableLauncher(cmdline, cmdline)()

start('echo-server.py')      # starts local server if it still haven't been started

args = ' '.join(sys.argv[1:])

for i in range(numclients):
    start('echo-client.py %s' % args)