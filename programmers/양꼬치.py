def solution(n, k):
    free_drink = n // 10
    answer = n * 12000 + (k - free_drink) * 2000
    return answer


def solution(n, k):
    return 12000 * n + 2000 * (k - n // 10)
