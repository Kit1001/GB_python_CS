import logging
import sys



log = logging.getLogger('client')
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stderr)
format_ = logging.Formatter('%(levelname)-10s %(asctime)-30s %(module)-25s %(message)-20s')
handler.setFormatter(format_)
handler.setLevel(logging.DEBUG)
log.addHandler(handler)

if __name__ == '__main__':
    log.debug('debug')
    log.info('Hello, World!')
    log.warning('It seems to be a bug...')
    log.error('Error')
    log.critical('Critical bug in app!')