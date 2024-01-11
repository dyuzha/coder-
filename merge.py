# merge_sort


def merge(arr1: list, arr2: list, up=True) -> list:
    i = 0
    j = 0
    n1 = len(arr1)
    n2 = len(arr2)
    arr = []
    if (arr1[i] > arr[j]) == up:
        arr.append(arr1[i])
    else:
        arr.append(arr2[j])
        

