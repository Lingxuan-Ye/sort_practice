"""
Python 的二分查找算法实现详见 `bisect` 模块.
"""
import bisect
from typing import Any, Callable

import testutils


@testutils.timer
def _binary_search(list_: list, value: int) -> int:
    """
    Assume lst is an ascending list.

    Returns
    -------
    int
        Index of value.
        Returns -1 if no result.
    """
    lower: int = 0
    upper: int = len(list_) - 1
    if value < list_[lower] or value > list_[upper]:
        return -1
    while lower <= upper:
        mid = (upper - lower) // 2
        mid_value = list_[mid]
        if value ==mid_value:
            return mid
        elif value < mid_value:
            upper = mid - 1
        else:
            lower = mid + 1
    return -1


@testutils.timer
def binary_search(list_: list, value: int) -> int:
    """
    Find first occurence.
    Assume lst is an ascending list.

    Returns
    -------
    int
        Index of value.
        Returns -1 if no result.
    """
    # lower: int = 0
    # upper: int = len(list_) - 1
    # if value < list_[lower] or value > list_[upper]:
    #     return -1
    # while lower <= upper:
    #     mid = (upper - lower) // 2
    #     mid_value = list_[mid]
    #     if value ==mid_value:
    #         return mid
    #     elif value < mid_value:
    #         upper = mid - 1
    #     else:
    #         lower = mid + 1
    # return -1


# if __name__ == "__main__":
#     from random import randrange
#     testlist = [randrange(0, 1_000_000) for _ in range(1_000_000)]
