def solution(my_string):
    return "".join(dict.fromkeys(my_string))


def solution(my_string):
    answer = ""
    for i in my_string:
        if i not in answer:
            answer += i
    return answer
