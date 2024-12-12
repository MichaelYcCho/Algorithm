def solution(arr):
    answer = []

    for i in arr:
        if i % 2 == 0 and i >= 50:
            answer.append(int(i / 2))
        elif i % 2 == 1 and i <= 50:
            answer.append(i * 2)
        else:
            answer.append(i)

    return answer


def solution(arr):
    answer = []

    for item in arr:
        if item >= 50 and not item % 2:
            answer.append(item // 2)
        elif item < 50 and item % 2:
            answer.append(item * 2)
        else:
            answer.append(item)

    return answer
