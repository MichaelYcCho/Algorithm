def solution(my_string, m, c):
    answer = ""
    for i in range(0, len(my_string), m):
        w = my_string[i : i + m]
        print(w)
        answer += w[c - 1]
    return answer


def solution(my_string, m, c):
    answer = ""

    for i in range(0, len(my_string)):
        if i % m == 0:
            answer += my_string[i + c - 1]

    return answer
