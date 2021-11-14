import functools
from datetime import datetime


def check_time(msg):
    print(msg)
    def internal(func):
        @functools.wraps(func)
        def deco(*args, **kwargs):
            now = datetime.now()
            result = func(*args, *kwargs)
            print(datetime.now() - now)
            return result
        return deco
    return internal


@check_time('Hello')
def mult_func(a, b, c, d):
    """multiply function"""
    res = a * b * c * d
    return res


print(mult_func(10, 20, 20000, 3000))
print(mult_func.__name__)
print(mult_func.__doc__)
