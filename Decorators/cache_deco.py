import functools
import time


def profile(f):
    @functools.wraps(f)
    def deco(*args):
        start = time.time()
        result = f(*args)
        print(f'Elapsed time for function {f.__name__}: {time.time() - start}ms')
        return result
    return deco


def cache(n):
    def internal(f):
        @functools.wraps(f)
        def deco(*args):
            if args in deco._cache:
                return deco._cache[args]
            if len(deco._cache) == n:
                deco._cache.popitem()
            result = f(*args)
            deco._cache[args] = result
            print(deco._cache)
            return result
        deco._cache = {}
        return deco
    return internal


@profile
@cache(3)
def foo(n):
    time.sleep(n)


foo(1)
foo(2)
foo(3)
foo(4)
foo(5)
foo(1)
foo(2)
foo(3)
foo(4)
foo(5)
