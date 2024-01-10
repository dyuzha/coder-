import random as r


def randArr(n: int, float = False, start = -99, end = 99) -> list:
    if float:
        arr = [r.uniform(start, end) for i in range(n)]
    else:
        arr = [r.randint(start, end) for i in range(n)]
    return arr


def insertionSort(arr: list, reverse=True) -> None:
    n = len(arr)
    
    for i in range(1, n):
        j = i - 1
        flag = 0
        while j >= 0 and flag == 0:
            if (arr[i] > arr[j]) == reverse:
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
                i -= 1
            else:
                flag = 1






