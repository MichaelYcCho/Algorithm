def solution(num, n):
    answer = 0

    if num % n == 0:
        answer = 1
    else:
        answer = 0

    return answer


def solution(num, n):
    return int(not (num % n))
