def solution(n):
    a = 0
    if n % 2 == 1:
        for i in range(n, 0, -2):
            a += i
    else:
        for i in range(n, 0, -2):
            a += i**2
    return a


def solution(n):
    return (
        sum([i**2 for i in range(2, n + 1) if i % 2 == 0])
        if n % 2 == 0
        else sum([i for i in range(1, n + 1) if i % 2 == 1])
    )
