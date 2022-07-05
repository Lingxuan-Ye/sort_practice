from timer import timer


def partition(lst: list, lower: int, upper: int):
    temp = lst[lower]
    while lower < upper:
        while lower < upper and lst[upper] >= temp:
            upper -= 1
        lst[lower] = lst[upper]
        while lower < upper and lst[lower] <= temp:
            lower += 1
        lst[upper] = lst[lower]
    lst[lower] = temp
    return lower


def _quick_sort_recursive(lst: list, lower: int, upper: int):
    if lower < upper:
        mid = partition(lst, lower, upper)
        _quick_sort_recursive(lst, lower, mid - 1)
        _quick_sort_recursive(lst, mid + 1, upper)


@timer
def quick_sort_recursive(lst: list):
    if not lst:
        return
    _quick_sort_recursive(lst, 0, len(lst) - 1)


class Node:

    def __init__(self, lower: int, upper: int) -> None:
        self.lower: int = lower
        self.upper: int = upper


@timer
def quick_sort_non_recursive_Node(lst: list):
    if not lst:
        return
    temp = [Node(0, len(lst) - 1)]
    while temp:
        node = temp.pop()
        mid = partition(lst, node.lower, node.upper)
        if node.lower < mid - 1:
            temp.append(Node(node.lower, mid - 1))
        if mid + 1 < node.upper:
            temp.append(Node(mid + 1, node.upper))


@timer
def quick_sort_non_recursive_tuple(lst: list):
    if not lst:
        return
    temp = [(0, len(lst) - 1)]
    while temp:
        node = temp.pop()
        mid = partition(lst, node[0], node[1])
        if node[0] < mid - 1:
            temp.append((node[0], mid - 1))
        if mid + 1 < node[1]:
            temp.append((mid + 1, node[1]))


quick_sort = quick_sort_non_recursive_tuple

if __name__ == "__main__":

    import random

    lst = [random.randrange(0, 1_000_000) for i in range(1_000_000)]
    lst_ = [*lst]
    lst__ = [*lst]
    # print(lst == lst_ == lst__)
    # print(lst)
    quick_sort_recursive(lst)
    quick_sort_non_recursive_Node(lst_)
    quick_sort_non_recursive_tuple(lst__)
    # print(lst)

# 总结

# - 控制变量以后, 快速排序的非递归实现 `quick_sort_non_recursive_tuple` 相较于
#   递归实现 `quick_sort_recursive` 略快.

# - `quick_sort_non_recursive_Node` 明显慢于前两者, 这可能是 `Node` 实例化所致.

# - 递归深度为 n 并非意味着函数只能递归调用 n 次,
#   以每层递归调用两次为例, 实际最多可调用 2 ^ (n + 1) - 2 次,
#   当 n = 996 时, 共可调用约 6.70e299 次.
#   因此, 不必过多考虑将递归转为非递归实现.
