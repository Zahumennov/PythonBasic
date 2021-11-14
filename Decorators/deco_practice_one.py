import functools
from datetime import datetime


def time_check(msg):
    print(msg)
    def internal(func):
        @functools.wraps(func)
        def deco(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return deco
    return internal


@time_check("Hi")
def my_func(num):
    """Exponentiation function"""
    return num ** 10000


print(my_func(2))












