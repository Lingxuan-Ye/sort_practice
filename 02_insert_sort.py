import testutils


@testutils.timer
def insert_sort(lst: list):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > temp:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp


if __name__ == "__main__":
    testutils.test(insert_sort)
