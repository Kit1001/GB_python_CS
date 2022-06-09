from socket import *

from common.utils import *


def form_presence(username, status="Just connected"):
    presence = {"action": "presence",
                "type": "status",
                "user": {
                    "account_name": username,
                    "status": status
                }}
    return presence


def form_message(to="guest", from_="guest", message="Hello world"):
    message = {
        "action": "msg",
        "to": to,
        "from": from_,
        "message": message
    }
    return message


def response_handler(response):
    status = response['response']
    if status == 200:
        print('success')
        return response['payload']
    else:
        raise Exception(f'unknown error: code {status}')


s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))

username = input('Enter your username: ')
msg = form_presence(username)
s.send(wrap(msg))
response = s.recv(1024)
response = unwrap(response)
response_handler(response)
s.close()

# Presence established, run CLI interface
while True:
    command = input('type your command:\n')
    command = command.split(' ')
    command_type = command[0].strip()

    s = create_connection(('localhost', 8888))

    if command_type == 'presence':
        request = form_presence(username)
        request = json.dumps(request).encode()
        s.send(request)
        response = s.recv(1024)
        response = json.loads(response)
        print(response)

    elif command_type == 'send':
        to = command[1]
        message = " ".join(command[2:])
        request = form_message(to, from_=username, message=message)
        request = wrap(request)
        s.send(request)
        response = s.recv(1024)
        response = unwrap(response)
        response_handler(response)

    elif command_type == 'read':
        request = {
            "action": "get_msgs",
            "user": {
                "username": username
            },
        }
        request = wrap(request)
        s.send(request)
        response = s.recv(1024)
        response = unwrap(response)
        messages = response_handler(response)
        if len(messages) > 0:
            for msg in messages:
                print(f'New message from {msg["from"]}:\n {msg["message"]}')

    elif command_type == 'exit':
        s.close()
        break

    else:
        print('unknown command')

    s.close()
