# https://school.programmers.co.kr/learn/courses/30/lessons/12954


def solution(x, n):
    answer = []
    for i in range(1, n + 1):
        answer.append(x * i)
    return answer


def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]


print(number_generator(2, 5))
