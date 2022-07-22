import testutils


def sift(lst: list, lower: int, upper: int):
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
    temp = lst[lower]  # avoid unnecesary substitution
    parent = lower
    child = 2 * parent + 1  # left child
    while child <= upper:
        if child + 1 <= upper and lst[child] < lst[child + 1]:
            child += 1  # right child
        if temp >= lst[child]:
            break
        else:
            lst[parent] = lst[child]
            parent = child
            child = 2 * parent + 1
    lst[parent] = temp


@testutils.timer
def heap_sort(lst: list):
    # get max-heap
    last_leaf = len(lst) - 1
    parent = (last_leaf - 1) // 2
    while parent >= 0:
        sift(lst, parent, last_leaf)
        parent -= 1

    # sort
    while last_leaf > 0:
        lst[0], lst[last_leaf] = lst[last_leaf], lst[0]
        last_leaf -= 1
        sift(lst, 0, last_leaf)


if __name__ == "__main__":
    testutils.test(heap_sort, length=1_000_000)
