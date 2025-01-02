def solution(num, k):
    a = str(num).find(str(k))
    return a if a == -1 else a + 1


def solution(num, k):
    for i, n in enumerate(str(num)):
        if str(k) == n:
            return i + 1
    return -1
