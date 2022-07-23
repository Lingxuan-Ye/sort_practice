"""
Python 的堆队列算法实现详见 `heapq` 模块, 该模块只实现了 min-heap.
"""

import testutils


def sift(list_: list, lower: int, upper: int):
    """
    Assume left-subtree and right-subtree are already a max-heap.

    Parameters
    ----------
    lst : list
    lower : int
        Root index.
    upper : int
        Last leaf index.
    """
    temp = list_[lower]  # avoid unnecesary substitution
    parent = lower
    child = 2 * parent + 1  # left child
    while child <= upper:
        if child + 1 <= upper and list_[child] < list_[child + 1]:
            child += 1  # right child
        if temp >= list_[child]:
            break
        else:
            list_[parent] = list_[child]
            parent = child
            child = 2 * parent + 1
    list_[parent] = temp


@testutils.timer
def heap_sort(list_: list):
    # get max-heap
    last_leaf = len(list_) - 1
    parent = (last_leaf - 1) // 2
    while parent >= 0:
        sift(list_, parent, last_leaf)
        parent -= 1

    # sort
    while last_leaf > 0:
        list_[0], list_[last_leaf] = list_[last_leaf], list_[0]
        last_leaf -= 1
        sift(list_, 0, last_leaf)


if __name__ == "__main__":
    testutils.sort_test(heap_sort, length=1_000_000)

# 总结

# - 堆排序的时间复杂度为 O(nlogn), 但是在实际表现上要慢于快速排序.
