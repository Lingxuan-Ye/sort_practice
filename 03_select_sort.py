import testutils


@testutils.timer
def select_sort(list_: list):
    length = len(list_)
    for i in range(length - 1):
        selected = i
        for j in range(i + 1, length):
            if list_[j] < list_[selected]:
                selected = j
        list_[i], list_[selected] = list_[selected], list_[i]


if __name__ == "__main__":
    testutils.sort_test(select_sort)
