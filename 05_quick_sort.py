import testutils


def partition(list_: list, lower: int, upper: int):
    temp = list_[lower]
    while lower < upper:
        while lower < upper and list_[upper] >= temp:
            upper -= 1
        list_[lower] = list_[upper]
        while lower < upper and list_[lower] <= temp:
            lower += 1
        list_[upper] = list_[lower]
    list_[lower] = temp  # at this point, lower == upper
    return lower


def _quick_sort_recursive(list_: list, lower: int, upper: int):
    if lower < upper:
        mid = partition(list_, lower, upper)
        _quick_sort_recursive(list_, lower, mid - 1)
        _quick_sort_recursive(list_, mid + 1, upper)


@testutils.timer
def quick_sort_recursive(list_: list):
    if not list_:
        return
    _quick_sort_recursive(list_, 0, len(list_) - 1)


class Node:

    def __init__(self, lower: int, upper: int) -> None:
        self.lower: int = lower
        self.upper: int = upper


@testutils.timer
def quick_sort_non_recursive_Node(list_: list):
    if not list_:
        return
    temp = [Node(0, len(list_) - 1)]
    while temp:
        node = temp.pop()
        mid = partition(list_, node.lower, node.upper)
        if node.lower < mid - 1:
            temp.append(Node(node.lower, mid - 1))
        if mid + 1 < node.upper:
            temp.append(Node(mid + 1, node.upper))


@testutils.timer
def quick_sort_non_recursive_tuple(list_: list):
    if not list_:
        return
    temp = [(0, len(list_) - 1)]
    while temp:
        node = temp.pop()
        mid = partition(list_, node[0], node[1])
        if node[0] < mid - 1:
            temp.append((node[0], mid - 1))
        if mid + 1 < node[1]:
            temp.append((mid + 1, node[1]))


quick_sort = quick_sort_non_recursive_tuple

if __name__ == "__main__":
    testutils.sort_test(
        quick_sort_recursive,
        quick_sort_non_recursive_Node,
        quick_sort_non_recursive_tuple,
        length=1_000_000
    )

# 总结

# - 快速排序的时间复杂度为 O(nlogn)

# - 控制变量以后, 快速排序的非递归实现 `quick_sort_non_recursive_tuple` 相较于
#   递归实现 `quick_sort_recursive` 无明显区别.

# - `quick_sort_non_recursive_Node` 明显慢于前两者, 这可能是 `Node` 实例化所致.

# - 递归深度为 n 并非意味着函数只能递归调用 n 次,
#   以每层递归调用两次为例, 实际最多可调用 2 ^ (n + 1) - 2 次,
#   当 n = 996 时, 共可调用约 6.70e299 次.
#   因此, 不必过多考虑将递归转为非递归实现.
