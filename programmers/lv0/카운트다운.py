def solution(start, end_num):
    return [i for i in range(start, end_num - 1, -1)]


def solution(start, end):
    answer = []
    while start >= end:
        answer.append(start)
        start -= 1
    return answer
