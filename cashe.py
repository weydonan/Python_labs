cache_dict = {}


def cache(func):
    def wrapper(*args):
        if args in cache_dict:
            return cache_dict[args]
        result = func(*args)
        cache_dict[args] = result
        return result

    return wrapper


@cache
def fact(n):
    if n == 0: return 1
    return n * fact(n - 1)


for i in range(0, 100):
    fact(i)
print(fact(5))
