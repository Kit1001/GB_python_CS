import inspect
import logging
from functools import wraps

import log.client_log_config
import log.server_log_config


def logdec(func):
    logger = logging.getLogger('server')
    stack = inspect.stack()
    module = stack[-1].filename.split("/")[-1].strip(".py")

    @wraps(func)
    def wrapper(*args):
        string = f'"{func.__name__}" is called '
        for i in range(1, len(stack) - 1):
            string = f'{string}from function "{stack[i].function}" '

        string = f'{string}from module "{module}"'
        logger.debug(string)
        result = func(*args)
        return result

    return wrapper



