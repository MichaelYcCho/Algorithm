def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]


def solution(arr):
    answer = []
    check = []
    if 2 not in arr:
        return [-1]
    else:
        for i in range(0, len(arr)):
            if arr[i] == 2:
                check.append(i)
    return arr[check[0] : check[-1] + 1]
