def solution(my_string, s, e):
    return my_string[:s] + my_string[s : e + 1][::-1] + my_string[e + 1 :]


def solution(my_string, s, e):
    answer = my_string[:s]
    for i in range(e, s - 1, -1):
        answer += my_string[i]
    answer += my_string[e + 1 :]
    return answer
