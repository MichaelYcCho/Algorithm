# https://school.programmers.co.kr/learn/courses/30/lessons/12934
# n의 1/2 제곱은 n의 제곱근이다.
def solution(n):
    x = n ** (1 / 2)
    if x % 1 == 0:
        answer = (x + 1) ** 2
    else:
        answer = -1

    return int(answer)


print(solution(121))
print(solution(3))


def next_squre(n):
    # sqrt 는 제곱근을 구하는 함수
    from math import sqrt

    return "no" if sqrt(n) % 1 else (sqrt(n) + 1) ** 2
