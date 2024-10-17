def solution(num_list):
    odd = sum([num_list[i] for i in range(0, len(num_list), 2)])
    even = sum([num_list[i] for i in range(1, len(num_list), 2)])
    return odd if odd > even else even


def solution(num_list):
    even = 0
    odd = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            even += num_list[i]
        elif i % 2 == 1:
            odd += num_list[i]
    if even > odd:
        return even
    else:
        return odd
