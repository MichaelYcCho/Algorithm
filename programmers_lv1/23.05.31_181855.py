# https://school.programmers.co.kr/learn/courses/30/lessons/181855

def solution(strArr):
    answer = [len(i) for i in strArr]
    tmp = []
    for i in set(answer):
        tmp.append(answer.count(i))
    
    return max(tmp)
