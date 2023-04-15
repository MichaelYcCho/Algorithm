def solution(n):
    answer = 0
    for i in range(1, n + 1):
        # i로 나누어 떨어지는 수는 약수이다.
        if n % i == 0:
            answer += i
    return answer
