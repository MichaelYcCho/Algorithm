def solution(a, d, included):
    total_sum = 0
    for i in range(len(included)):
        if included[i]:
            total_sum += a + d * i
    return total_sum


def solution(a, d, included):
    sequence = [a + d * i for i in range(len(included))]
    return sum(val for val, inc in zip(sequence, included) if inc)