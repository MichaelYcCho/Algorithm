def solution(array):
    return [max(array), array.index(max(array))]


def solution(array):
    return sorted([[a, i] for i, a in enumerate(array)])[::-1][0]
