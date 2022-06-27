import json

from .variables import *


def wrap(msg):
    return json.dumps(msg).encode(ENCODING)


def unwrap(msg):
    return json.loads(msg.decode(ENCODING))
