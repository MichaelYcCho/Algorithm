# https://school.programmers.co.kr/learn/courses/30/lessons/12916


def solution(s):
    p_count = y_count = 0
    for str in s:
        if str.upper() == "P":
            p_count += 1
        elif str.upper() == "Y":
            y_count += 1

    return bool(p_count == y_count)


# count를 사용해서 더 간단하게 가능
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count("p") == s.lower().count("y")
