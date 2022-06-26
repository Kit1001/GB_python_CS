import atexit
from socket import *
from threading import Thread


def receiver(socket):
    while True:
        msg = socket.recv(1024).decode('UTF-8')
        print(f'received: {msg}')


def transmitter(socket):
    while True:
        msg = input()
        socket.send(msg.encode('UTF-8'))


sock = socket(AF_INET, SOCK_STREAM)
atexit.register(lambda: sock.close())
sock.connect(('', 8889))

t = Thread(target=receiver, args=(sock,))
i = Thread(target=transmitter, args=(sock,))
t.daemon = False
t.start()
i.start()
