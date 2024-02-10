def solution(n):
    answer = 0
    for i in range(1, n + 1):
        # i로 나누어 떨어지는 수는 약수이다.
        if n % i == 0:
            answer += i
    return answer


def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
