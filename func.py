import random as r

def randArr(n: int, float = False, start = -99, end = 99) -> list:
    if float:
        arr = [r.uniform(start, end) for i in range(n)]
    else:
        arr = [r.randint(start, end) for i in range(n)]
    return arr

arr = randArr(10, float=True)

print(arr)