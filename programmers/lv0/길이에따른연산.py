def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        for i in num_list:
            answer += i
    else:
        answer += 1
        for i in num_list:
            answer *= i
    return answer


def solution(num_list):
    if len(num_list) >= 11:
        return eval("+".join(list(map(str, num_list))))
    else:
        return eval("*".join(list(map(str, num_list))))
