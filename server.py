import select
from socket import *
import atexit

sock = socket(AF_INET, SOCK_STREAM)
atexit.register(lambda: sock.close())
sock.bind(('', 8889))
sock.listen(5)
sock.settimeout(1)
all_clients = []
message_queue = []

while True:
    try:
        conn, addr = sock.accept()
    except timeout as e:
        pass
    else:
        all_clients.append(conn)
    finally:
        # r = []
        # w = []

        r, w, e = select.select(all_clients, all_clients, [], 0)

        for client in r:
            try:
                msg = client.recv(1024).decode('UTF-8')
                if msg == '':
                    all_clients.remove(client)
                message_queue.append(msg)
            except Exception as e:
                print(e)
                all_clients.remove(client)

        # print(w)
        condition = len(message_queue) > 0
        for client in w:

            try:
                # отправляем время клиенту
                # print('trying to send message')
                # if len(message_queue) > 0: print(message_queue)
                if condition:
                    msg = message_queue[-1]
                    client.send(msg.encode('utf-8'))
                    print('message sent')
            except Exception:
                all_clients.remove(client)

        if condition:
            message_queue.pop()
