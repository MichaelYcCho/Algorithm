def solution(num_list, n):
    return [num_list[i] for i in range(0, len(num_list), n)]


def solution(num_list, n):
    return num_list[::n]


def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i])
    return answer
