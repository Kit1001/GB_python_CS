import logging
import os
import sys
from logging import handlers

from GB_pyhton_CS.common.variables import ENCODING

log = logging.getLogger('server')
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stderr)
format_ = logging.Formatter('%(levelname)-10s %(asctime)-30s %(module)-25s %(message)-20s')
handler.setFormatter(format_)
handler.setLevel(logging.DEBUG)
log.addHandler(handler)


path = os.path.join(os.path.dirname(__file__), "logs")
path = os.path.join(path, "server")
path = os.path.join(path, "server.log")
file_handler = handlers.TimedRotatingFileHandler(path, when="midnight", interval=1, encoding=ENCODING)
file_handler.setFormatter(format_)
file_handler.setLevel(logging.WARNING)
log.addHandler(file_handler)

if __name__ == '__main__':
    log.debug('debug')
    log.info('Hello, World!')
    log.warning('It seems to be a bug...')
    log.error('Error')
    log.critical('Critical bug in app!')
