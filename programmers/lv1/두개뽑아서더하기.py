from itertools import combinations


def solution(numbers):
    answer = set()
    for i in list(combinations(numbers, 2)):
        answer.add(sum(i))
    return sorted(answer)


def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))


def solution(numbers):
    answer = []
    l = len(numbers)
    for i in range(l):
        for j in range(l):
            if i != j:
                answer.append(numbers[i] + numbers[j])

    return sorted(list(set(answer)))
