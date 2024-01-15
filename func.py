import random as r


def randArr(n: int, float = False, start = -99, end = 99) -> list:
    if float:
        list = [r.uniform(start, end) for i in range(n)]
    else:
        list = [r.randint(start, end) for i in range(n)]
    return list



def insertionSort(lst: list, reverse=False) -> None:
    n = len(lst)
    for i in range(1, n):
        j = i - 1
        while j >= 0:
            if (lst[i] > lst[j]) == reverse:
                lst[i], lst[j] = lst[j], lst[i]
                j -= 1
                i -= 1
            else:
                break


def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = temp




arr = randArr(10)
print(arr)
print()
insertionSort(arr)
print(arr)

