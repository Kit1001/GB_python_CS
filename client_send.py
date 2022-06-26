import atexit
from socket import *


sock = socket(AF_INET, SOCK_STREAM)
atexit.register(lambda: sock.close())
sock.connect(('', 8889))


while True:
    msg = input('Ваше сообщение: ')
    sock.send(msg.encode('UTF-8'))
