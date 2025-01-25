def solution(num_list):
    num_list.sort()
    return num_list[:5]


def solution(num_list):
    answer = []
    for i in range(5):

        answer.append(min(num_list))
        num_list.remove(min(num_list))
    return answer
