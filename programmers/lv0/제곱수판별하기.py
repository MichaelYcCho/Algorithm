def solution(n):
    sqrt = n ** (1 / 2)
    if sqrt % 1 == 0:
        return 1
    else:
        return 2


def solution(n):
    return 1 if (n**0.5).is_integer() else 2
