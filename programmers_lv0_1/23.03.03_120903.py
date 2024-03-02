def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer


# set을 통해서 s1과 s2의 중복된 문자열의 교집합을 반환한후, 해당 값들의 길이(len)를 반환한다.
def solution(s1, s2):
    answer = len(set(s1) & set(s2))
    return answer