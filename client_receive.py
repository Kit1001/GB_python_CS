import atexit
from socket import *


sock = socket(AF_INET, SOCK_STREAM)
atexit.register(lambda: sock.close())
sock.connect(('', 8889))


while True:
    msg = sock.recv(1024).decode('UTF-8')
    print(f'received: {msg}')
