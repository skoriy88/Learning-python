"""
############################################################################
запускает графические интерфейсы получения и отправки по ftp независимо
от каталога, в котором находится сценарий; сценарий не обязательно
должен находиться в os.getcwd; можно также жестко определить путь
в $PP4EHOME или guessLocation; можно было бы также так: [from PP4E.
launchmodes import PortableLauncher, PortableLauncher('getfilegui', '%s/
getfilegui.py' % mydir)()], но в Windows понадобилось бы всплывающее
окно DOS для вывода сообщений о состоянии, описывающих выполняемые операции;
############################################################################
"""

import os, sys
print('Running in: ', os.getcwd())

from Tools.find import findlist
mydir = os.path.dirname(findlist('PyFtpGui.py', startdir=os.curdir)[0])

if sys.platform[:3] == 'win':
    os.system('start %s\getfilegui.py' % mydir)
    os.system('start %s\putfilegui.py' % mydir)
else:
    os.system('python %s/getfilegui.py &' % mydir)
    os.system('python %s/putfilegui.py &' % mydir)
