# https://school.programmers.co.kr/learn/courses/30/lessons/181870

def solution(strArr):
    result = []
    for string in strArr:
        if "ad" not in string:  # 문자열에 "ad"가 없는 경우
            result.append(string)
    return result