# https://school.programmers.co.kr/learn/courses/30/lessons/12912


def solution(a, b):
    answer = 0
    min_num = a
    max_num = b

    if a > b:
        min_num = b
        max_num = a

    for number in range(min_num, max_num + 1):
        answer += number

    return answer


# 최적의 식
def solution(a: int, b: int):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))
