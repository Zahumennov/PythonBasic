import functools


def cache_deco(max_length):
    def internal(func):
        @functools.wraps(func)
        def deco(*args, **kwargs):

            if args in deco.cache:
                return deco.cache[args]
            if len(deco.cache) == max_length:
                deco.cache.popitem()
            result = func(*args, kwargs)
            deco.cache[args] = result
            return result

        deco.cache = {}
        return deco
    return internal

