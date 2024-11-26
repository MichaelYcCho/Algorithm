def solution(a, b):
    answer = 0

    num1 = int(str(a) + str(b))
    num2 = 2 * a * b

    if num1 > num2:
        answer = num1
    elif num1 < num2:
        answer = num2
    else:
        answer = num1
    return answer


def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)
