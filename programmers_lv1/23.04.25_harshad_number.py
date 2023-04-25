# https://school.programmers.co.kr/learn/courses/30/lessons/12947


def solution(x):
    answer = False
    divide_num = 0
    for i in str(x):
        divide_num += int(i)

    if x % divide_num == 0:
        answer = True

    return answer
