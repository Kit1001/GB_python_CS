import atexit
from socket import *
from threading import Thread
from time import sleep

from common.utils import *


def establish_presence(s: socket, user: str) -> bool:
    presence = {"action": "presence",
                "type": "status",
                "user": {
                    "account_name": user,
                    "status": 'just connected'
                }}
    s.send(wrap(presence))
    response = unwrap(s.recv(1024))
    if response['response'] == 200:
        print('Successfully connected, you can type messages to chat now')
        return True
    else:
        print('Unknown error\n', response)
        return False


def receiver(s: socket):
    while True:
        msg = unwrap(s.recv(1024))
        message = msg['message']
        sender = msg['from']
        print(f'{sender}: {message}')


def transmitter(s: socket, user):
    while True:
        msg = input()
        message = {
            "action": "msg",
            "to": None,
            "from": user,
            "message": msg
        }
        s.send(wrap(message))


username = input('Enter your nickname: ')

sock = socket(AF_INET, SOCK_STREAM)
atexit.register(lambda: sock.close())
sock.connect((DEFAULT_ADDRESS, DEFAULT_PORT))

connection = establish_presence(sock, username)

if connection:
    t = Thread(target=receiver, args=(sock,))
    i = Thread(target=transmitter, args=(sock, username, ))
    t.daemon, i.daemon = True, True
    t.start()
    i.start()

while True:
    sleep(1)
