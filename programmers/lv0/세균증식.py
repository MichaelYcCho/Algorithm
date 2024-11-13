def solution(n, t):
    answer = n
    for time in range(t):
        answer *= 2
    return answer
