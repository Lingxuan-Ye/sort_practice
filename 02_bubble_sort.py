import testutils


@testutils.timer
def bubble_sort(lst: list):
    length = len(lst)
    has_exchange = False
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                has_exchange = True
        if not has_exchange:
            return


if __name__ == "__main__":
    testutils.sort_test(bubble_sort)
