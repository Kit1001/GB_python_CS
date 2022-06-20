import inspect
import logging
from functools import wraps

import log.client_log_config
import log.server_log_config


def log_this(func):
    stack = inspect.stack()
    module = stack[-1].filename.split("/")[-1].strip(".py")
    logger = logging.getLogger(module)

    @wraps(func)
    def wrapper(*args, **kwargs):
        string = f'"{func.__name__}" is called '
        for i in range(1, len(stack) - 1):
            string = f'{string}from function "{stack[i].function}" '

        string = f'{string}from module "{module}"'
        logger.debug(string, extra={'real_module': module})
        result = func(*args, **kwargs)
        return result

    return wrapper
