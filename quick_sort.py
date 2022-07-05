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


@timer
def quick_sort(lst: list, lower: int, upper: int):
    if lower < upper:
        mid = partition(lst, lower, upper)
        quick_sort(lst, lower, mid - 1)
        quick_sort(lst, mid + 1, upper)
