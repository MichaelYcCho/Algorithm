def solution(my_string):
    # 1. 접미사 리스트 생성
    suffixes = [my_string[i:] for i in range(len(my_string))]
    # 2. 사전순 정렬
    suffixes.sort()
    return suffixes


def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[-1 - i :])
    answer.sort()
    return answer
