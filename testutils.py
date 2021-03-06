from functools import wraps
from random import shuffle
from time import time
from typing import Callable, List, Union


def timer(arg: Union[int, Callable]):
    if isinstance(arg, int):
        def decorator(func: Callable):
            @wraps(func)
            def wrapper(*args, **kwargs):
                result = []
                before = time()
                for _ in range(arg):
                    result.append(func(*args, **kwargs))
                after = time()
                print(f"runtime = {after - before} seconds")
                if any(i is not None for i in result):
                    return result
            return wrapper
        return decorator
    else:
        func = arg
        @wraps(func)
        def wrapper(*args, **kwargs):
            before = time()
            result = func(*args, **kwargs)
            after = time()
            print(f"runtime = {after - before} seconds")
            return result
        return wrapper


def _abbr(lst: list):
    return str(lst[:20]) + "\b, ...]"


def sort_test(*func: Callable[[list], list | None], length: int = 1_000):
    testlist = [i for i in range(length)]
    shuffle(testlist)
    print("raw:\n" + _abbr(testlist), end="\n\n")
    result: List[list] = []
    for i in func:
        list_i = testlist.copy()
        result_i = i(list_i)
        print("\n", end="")
        result.append(list_i if result_i is None else result_i)
    if len(result) == 1:
        print("ordered:")
        print(_abbr(result[0]))
    elif all(result[0] == i for i in result[1:]):
        print("results are all the same", end="\n\n")
        print("ordered:")
        print(_abbr(result[0]))
    else:
        print("results are not all the same", end="\n\n")
        print("results:")
        for j, k in enumerate(result):
            print(f"{j}: {_abbr(k)}")
