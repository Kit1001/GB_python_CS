import logging
import os
import sys

log = logging.getLogger('client')
log.setLevel(logging.DEBUG)


stream_handler = logging.StreamHandler(sys.stderr)
format_ = logging.Formatter('%(levelname)-10s %(asctime)-30s %(module)-25s %(message)-20s')
stream_handler.setFormatter(format_)
stream_handler.setLevel(logging.DEBUG)
log.addHandler(stream_handler)

path = os.path.join(os.path.dirname(__file__), "logs")
path = os.path.join(path, "client")
path = os.path.join(path, "client.log")
file_handler = logging.FileHandler(path)
file_handler.setFormatter(format_)
file_handler.setLevel(logging.WARNING)
log.addHandler(file_handler)


if __name__ == '__main__':
    log.debug('debug')
    log.info('Hello, World!')
    log.warning('It seems to be a bug...')
    log.error('Error')
    log.critical('Critical bug in app!')
