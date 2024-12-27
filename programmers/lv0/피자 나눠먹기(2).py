def solution(n):
    tmp = 6 / n

    for i in range(1, 101):
        if (tmp * i).is_integer():
            answer = i
            break

    return answer


def solution(n):
    i = 1
    while 1:
        if (6 * i) % n == 0:
            return i
        i += 1
