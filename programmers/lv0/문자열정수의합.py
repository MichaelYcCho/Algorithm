def solution(num_str):
    answer = 0
    for i in num_str:
        answer += int(i)

    return answer


def solution(num_str):
    return sum(map(int, list(num_str)))
