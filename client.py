import logging
from socket import *

from GB_pyhton_CS.common.utils import *

logger = logging.getLogger('client')


def presence_constructor(username='guest', status="Just connected"):
    presence = {"action": "presence",
                "type": "status",
                "user": {
                    "account_name": username,
                    "status": status
                }}
    return presence


def message_constructor(to="guest", from_="guest", message="Hello world"):
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
        # print('success')
        logger.debug('Handler received response 200')
        return response['payload']
    else:
        raise ValueError(f'unknown error: code {status}')


if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(get_address())
    username = input('Enter your username: ')
    msg = presence_constructor(username)
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

        s = create_connection(get_address())

        # Simple CLI:
        # 'presence' establishes or renews client's presence on server
        # 'send user message' - send message to user
        # 'read' - print unread messages
        if command_type == 'presence':
            request = presence_constructor(username)
            request = json.dumps(request).encode()
            s.send(request)
            response = s.recv(1024)
            response = unwrap(response)
            # print(response)
            logger.debug(f'Server response: {response}')

        elif command_type == 'send':
            to = command[1]
            message = " ".join(command[2:])
            request = message_constructor(to, from_=username, message=message)
            request = wrap(request)
            s.send(request)
            response = s.recv(1024)
            response = unwrap(response)
            logger.debug(f'Server response: {response}')
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
                    logger.info(f'Got new message from {msg["from"]}')

        elif command_type == 'exit':
            s.close()
            break

        else:
            print('unknown command')
            logger.error(f'User passed an unknown command {command_type}')

        s.close()
