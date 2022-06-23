from socket import *


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('', 8889))

while True:
    msg = input('Ваше сообщение: ')
    sock.send(msg.encode('UTF-8'))
    data = sock.recv(1024).decode('UTF-8')
    print(data)