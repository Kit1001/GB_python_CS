from functools import wraps

import decos


def other_dec(func):

    @wraps(func)
    def wrapper(*args):
        return func(*args)
    return wrapper

def func_y():
    pass


@decos.logdec
def func_z():
    func_y()


def func_x():
    func_z()


def main():
    func_x()


main()