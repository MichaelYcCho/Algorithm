def solution(a, b, flag):
    answer = 0

    if flag == True:
        answer = a + b
    else:
        answer = a - b
    return answer


def solution(a, b, flag):
    if flag:
        return a + b
    return a - b
