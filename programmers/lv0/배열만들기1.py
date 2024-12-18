def solution(n, k):
    return [i for i in range(1, n + 1) if i % k == 0]


def solution(n, k):
    answer = []
    index = 1
    while k * index <= n:
        answer.append(k * index)
        index += 1
    return answer
