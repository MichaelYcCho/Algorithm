def solution(my_string, target):
    if target in my_string:
        return 1
    else:
        return 0


def solution(my_string, target):
    answer = 0

    my_string2 = list(my_string)

    for i in range(len(my_string)):
        if my_string2[: len(target)] == list(target):
            return 1
        my_string2.pop(0)

    return answer
