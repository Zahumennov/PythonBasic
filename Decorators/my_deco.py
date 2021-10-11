import functools
from datetime import datetime


def time_me(msg):
    def internal(func):
        @functools.wraps(func)
        def deco(*args):
            time_one = datetime.now()
            result = func(*args)
            print(msg, datetime.now() - time_one)
            return result
        return deco
    return internal


@time_me('Time:')
def some_foo(n, s):
    """Some help"""
    while n < s:
        print(n)
        n += 1
    return "Done"


print(some_foo(1, 5))
help(some_foo)

