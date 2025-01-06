def solution(str_list, ex):
    return "".join(i for i in str_list if ex not in i)


def solution(str_list, ex):
    filtered_list = [s for s in str_list if ex not in s]
    return "".join(filtered_list)
