from functools import wraps
from time import time
from typing import Callable


def timer(func: Callable):

    @wraps(func)
    def wrapper(*args, **kwargs):
        before = time()
        result = func(*args, **kwargs)
        after = time()
        print(f"runtime = {after - before} seconds")
        return result

    return wrapper
