def solution(n, numlist):
    array = []
    for i in numlist:
        if i % n == 0:
            array.append(i)
    return array



def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))