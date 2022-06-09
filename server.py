from socket import *
import time

from common.utils import *
# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument('adress', metavar='A', type=str, help='ip address')
# args = parser.parse_args()

def response_constructor(payload=None, code=200, **kwargs):
    response = {
        "response": code,
        "time": time.time(),
        "payload": payload
    }
    response.update(kwargs)
    print(response)
    return response


def request_handler(request):
    action = request['action']

    if action == 'presence':
        response = response_constructor("presence established", unread_messages=3)
        return response

    elif action == 'msg':
        # print(f'received message from {request["from"]} for {request["to"]}')
        # print(request['message'])
        request['time'] = time.time()
        message_queue.append(request)
        response = response_constructor("message recieved")
        return response

    elif action == 'get_msgs':
        username = request['user']['username']
        tmp_queue = []

        for message in message_queue:
            if message['to'] == username:
                tmp_queue.append(message)
                message['to_remove'] = True

        for message in tmp_queue:
            message_queue.remove(message)

        print(tmp_queue)
        response = response_constructor(payload=tmp_queue)
        return response


message_queue = []

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('', 8888))
s.listen(5)
while True:
    print(message_queue)
    client, addr = s.accept()
    try:
        request = client.recv(1024)
        if not request:
            client.close()
            continue
        request = unwrap(request)
        response = request_handler(request)
        response = wrap(response)
        client.send(response)
    except (BrokenPipeError, ConnectionResetError) as e:
        print(e, 'occurred')
    finally:
        client.close()
