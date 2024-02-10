def solution(n):
    answer = []
    for s in str(n):
        answer.append(int(s))

    answer.reverse()
    return answer


# print(solution(12345))


def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]


print("결과 : {}".format(digit_reverse(12345)))
