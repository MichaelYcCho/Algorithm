def solution(my_string):
    return "".join(sorted(list(my_string.lower())))


def solution(my_string):
    answer = []
    for i in my_string:
        if ord(i) >= ord("A") and ord(i) <= ord("Z"):
            answer.append(chr(ord(i) + 32))
        else:
            answer.append(i)
    return "".join(sorted(answer))
