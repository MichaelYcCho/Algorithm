def solution(num_list):
    num_list.sort()

    return num_list[5:]


def solution(num_list):
    for i in range(len(num_list)):
        j = len(num_list)
        for k in range(0, j):
            if num_list[i] < num_list[k]:
                temp = num_list[i]
                num_list[i] = num_list[k]
                num_list[k] = temp

    return num_list[5 : len(num_list)]
