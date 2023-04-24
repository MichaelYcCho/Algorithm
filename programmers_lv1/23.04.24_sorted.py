# https://school.programmers.co.kr/learn/courses/30/lessons/12933


def solution(n: int) -> int:
    return int("".join(sorted(str(n), reverse=True)))


print(solution(118372))
