import select
import time
from socket import *
import atexit

from GB_python_CS.common.utils import *
from GB_python_CS.common.variables import *


def request_handler(mq: list, request, client_socket):
    if request['action'] == 'presence':
        response = {
            "response": 200,
            "time": time.time(),
            "payload": 'success'
        }
        client_socket.send(wrap(response))
    elif request['action'] == 'msg':
        mq.append(request)


sock = socket(AF_INET, SOCK_STREAM)
atexit.register(lambda: sock.close())
sock.bind((DEFAULT_ADDRESS, DEFAULT_PORT))
sock.listen(10)
sock.settimeout(0.5)
all_clients = []
message_queue = []

while True:
    print(message_queue)
    try:
        conn, addr = sock.accept()
    except timeout as e:
        pass
    else:
        all_clients.append(conn)
    finally:
        r, w, e = select.select(all_clients, all_clients, [], 0)

        for client in r:
            try:
                msg = unwrap(client.recv(1024))
                if msg == '':
                    all_clients.remove(client)

                request_handler(message_queue, msg, client)
            except Exception as e:
                print(e)
                all_clients.remove(client)

        condition = len(message_queue) > 0
        for client in w:
            try:
                if condition:
                    msg = message_queue[-1]
                    client.send(wrap(msg))
                    print('message sent')
            except Exception:
                all_clients.remove(client)

        if condition:
            message_queue.pop()
