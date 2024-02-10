# https://school.programmers.co.kr/learn/courses/30/lessons/181903

def solution(q, r, code):
    result = ""
    for i, ch in enumerate(code):
        if i % q == r:  # 나머지가 r인 위치의 문자인 경우
            result += ch
    return result