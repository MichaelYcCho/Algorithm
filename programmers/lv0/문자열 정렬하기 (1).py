def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    answer.sort()
    return answer


def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])
