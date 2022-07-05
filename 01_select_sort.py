from timer import timer


@timer
def select_sort(lst: list):
    length = len(lst)
    for i in range(length - 1):
        selected = i
        for j in range(i + 1, length):
            if j < selected:
                selected = j
        lst[i], lst[selected] = lst[selected], lst[i]

