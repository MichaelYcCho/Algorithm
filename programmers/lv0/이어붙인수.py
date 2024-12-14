def solution(num_list):
    answer_1 = ""
    answer_2 = ""
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            answer_1 += str(num_list[i])
        else:
            answer_2 += str(num_list[i])
    answer = int(answer_1) + int(answer_2)
    return answer


def solution(num_list):
    even = int("".join([str(i) for i in num_list if i % 2 == 0]))
    odd = int("".join([str(i) for i in num_list if not i % 2 == 0]))
    return even + odd
