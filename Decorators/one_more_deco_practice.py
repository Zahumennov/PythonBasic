import functools
import time


def profile(func):
    @functools.wraps(func)
    def deco(*args):
        start = time.time()
        result = func(*args)
        print(f'Elapsed time for function {func.__name__}: {time.time() - start}ms')
        return result
    return deco


def cache(max_length):
    def internal(func):
        @functools.wraps(func)
        def deco(*args):
            if args in deco._cache:
                return deco._cache[args]
            if len(deco._cache) == max_length:
                deco._cache.popitem()
            result = func(*args)
            deco._cache[args] = result
            print(deco._cache)
            return result
        deco._cache = {}
        return deco
    return internal


@profile
@cache(10)
def foo(a):
    return a ** 100

foo(22)
foo(33)
foo(44)
foo(44)