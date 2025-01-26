def solution(arr, n):
    for i, a in enumerate(arr):
        if len(arr) % 2 != 0 and i % 2 == 0:
            arr[i] += n
        elif len(arr) % 2 == 0 and i % 2 != 0:
            arr[i] += n
    return arr


def solution(arr, n):
    N = len(arr)
    if N % 2:
        for i in range(0, N, 2):
            arr[i] += n
    else:
        for i in range(1, N, 2):
            arr[i] += n
    return arr
