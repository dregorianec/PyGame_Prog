import pyspeedtest

speed = pyspeedtest.SpeedTest('mail.ru')
print('Ping: ' + str(int(speed.ping())) + ' ms')
print('Download speed:' + str(int(pyspeedtest.SpeedTest('www.google.com').download() * 1024 // 1048576)) + ' kbps')
