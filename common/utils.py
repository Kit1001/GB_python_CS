import json

from .variables import ENCODING


def wrap(msg):
    return json.dumps(msg).encode(ENCODING)


def unwrap(msg):
    return json.loads(msg.decode(ENCODING))
