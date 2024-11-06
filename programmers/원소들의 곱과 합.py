def solution(num_list):
    answer = 1
    for i in num_list:
        answer *= i
    return 1 if answer < sum(num_list) ** 2 else 0


def solution(num_list):
    a = 1
    b = 0
    for x in num_list:
        a *= x
        b += x
    if a < b * b:
        return 1
    return 0
