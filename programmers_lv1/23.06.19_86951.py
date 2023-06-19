def solution(numbers):
    num=[1,2,3,4,5,6,7,8,9]
    a = list(set(num) - set(numbers)) # 차집합
    return sum(a)


def solution(numbers):
    return 45 - sum(numbers)


def solution(numbers):
    answer=0
    for i in range(1,10):
        if i not in numbers:
            answer += i
    return answer