def solution(hp):
    a = hp // 5
    b = (hp - (5 * a)) // 3
    c = (hp - (5 * a) - (b * 3)) // 1
    answer = a + b + c

    return answer


def solution(hp):
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
