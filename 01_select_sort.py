import testutils


@testutils.timer
def select_sort(lst: list):
    length = len(lst)
    for i in range(length - 1):
        selected = i
        for j in range(i + 1, length):
            if lst[j] < lst[selected]:
                selected = j
        lst[i], lst[selected] = lst[selected], lst[i]


if __name__ == "__main__":
    testutils.test(select_sort)
