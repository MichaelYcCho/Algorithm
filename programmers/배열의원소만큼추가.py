def solution(arr):
    answer = []

    for i in arr:
        for j in range(i):
            answer.append(i)

    return answer


def solution(arr):
    return [i for i in arr for j in range(i)]
