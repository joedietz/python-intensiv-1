"""
Decorators
"""

from functools import cache, wraps
from time import perf_counter, sleep


def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = f(*args, **kwargs)  # fn()
        end = perf_counter()
        print("Hat gedauert:", end - start)
        return result

    return wrapper


@timer
def fn(c, a, b):
    """Supertoller Docstring."""
    # aufwändiger JOb 2 Minuten
    print("dauert eine Zeit...")
    sleep(0.3)
    return 42


# print("Name der Funtkion:", fn.__name__)
# fn = timer(fn)
# print("Name der Funtkion:", fn.__name__, fn.__doc__)

result = fn(44, a=1, b=2)
print(f"Result der Funktion: {result}")

# start = perf_counter()
# fn()
# end = perf_counter()
# print("Hat gedauert:", end - start)
