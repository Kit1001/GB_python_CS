import select
from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8889))
sock.listen(5)
sock.settimeout(0.1)
all_clients = []
data = ''

while True:
    try:
        conn, addr = sock.accept()
    except timeout as e:
        pass
    else:
        all_clients.append(conn)
    finally:
        r = []
        w = []
        r, w, e = select.select(all_clients, all_clients, [], 0)


        # for client in r:
        #     try:
        #         msg = client.recv(1024).decode('UTF-8')
        #         # if msg == '':
        #         #     all_clients.remove(client)
        #         data = msg
        #     except Exception as e:
        #         print(e)
        #         # all_clients.remove(client)
        #
        # for client in w:
        #     try:
        #         # отправляем время клиенту
        #         client.send(data.encode('utf-8'))
        #         data = ''
        #     except Exception:
        #         # клиент отключился
        #         # all_clients.remove(client)
        #         pass