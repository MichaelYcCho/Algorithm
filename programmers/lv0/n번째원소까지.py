def solution(num_list, n):
    return num_list[0:n]


def solution(num_list, n):
    return [v for i, v in enumerate(num_list) if i < n]
