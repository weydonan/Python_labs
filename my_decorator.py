import os


def cache(filepath, key_type='positional'):
    def decorator(func):
        cache_storage = {}

        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.strip():
                            key_str, value_str = line.strip().split('|||')
                            key = eval(key_str)
                            value = eval(value_str)
                            cache_storage[key] = value
            except (ValueError, SyntaxError):
                pass

        def wrapper(*args, **kwargs):
            if key_type == 'positional':
                key = args
            elif key_type == 'named':
                key = tuple(sorted(kwargs.items()))
            elif key_type == 'both':
                key = (args, tuple(sorted(kwargs.items())))
            else:
                key = args

            if key in cache_storage:
                return cache_storage[key]

            result = func(*args, **kwargs)
            cache_storage[key] = result

            with open(filepath, 'w', encoding='utf-8') as f:
                for k, v in cache_storage.items():
                    f.write(f"{repr(k)}|||{repr(v)}\n")

            return result

        return wrapper

    return decorator


@cache('sum_cache.txt', key_type='positional')
def slow_sum(a, b):
    import time
    time.sleep(2)
    return a + b


@cache('multiply_cache.txt', key_type='both')
def multiply(x, y, z=1):
    return x * y * z


print(slow_sum(2, 3))
print(slow_sum(2, 3))
print(slow_sum(4, 5))

print(multiply(3, 4))
print(multiply(3, 4, z=2))
print(multiply(3, 4))