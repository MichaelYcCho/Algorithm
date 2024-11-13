def solution(n_str):
    return n_str.lstrip("0")


def solution(n_str):
    return str(int(n_str))


def solution(n_str):
    for i in range(len(n_str)):
        if n_str[i] != "0":
            return n_str[i:]
