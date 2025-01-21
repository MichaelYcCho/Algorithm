def solution(n):
    return str(n)


def solution(n):
    answer = ""

    if n >= 1 and n <= 10000:
        answer = str(n)
    else:
        raise ValueError("n is allowed between 1 ~ 10000!")

    return answer
