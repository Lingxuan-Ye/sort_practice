import testutils


@testutils.timer
def insert_sort(list_: list):
    for i in range(1, len(list_)):
        temp = list_[i]
        j = i - 1
        while j >= 0 and list_[j] > temp:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = temp


if __name__ == "__main__":
    testutils.sort_test(insert_sort)
