"""
your e-mail configuration
"""

popservername = 'pop.gmail.com'
popusername = input('Enter e-mail address: ')
smtpservername = 'smtp.gmail.com'
myaddress = popusername
mysignature = ('Testing...')
smtpuser = popusername
smtppasswdfile = ''
poppasswdfile = ''
sentmailfile = r'D:\tmp\sentmail.txt'
savemailfile = r'D:\tmp\savemail.txt'
fetchEncoding = 'utf8'
headersEncodeTo = None
fetchlimit = 25