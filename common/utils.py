import argparse
import json

from .variables import *


def wrap(msg):
    return json.dumps(msg).encode(ENCODING)


def unwrap(msg):
    return json.loads(msg.decode(ENCODING))


def get_address():
    parser = argparse.ArgumentParser()
    parser.add_argument('address', nargs="?", default=DEFAULT_ADDRESS)
    parser.add_argument('port', nargs="?", default=DEFAULT_PORT)
    args = parser.parse_args()
    return args.address, args.port
