def solution(t, p):
    answer = 0
    p_len = len(p)
    t_len = len(t)
    p = int(p)
    for i in range(0, t_len + 1 - p_len):
        if int(t[i : i + p_len]) <= p:
            answer += 1
    return answer


def solution(t, p):
    list = []
    l = len(p)
    count = 0
    for i in range(len(t)):
        if len(t[i : i + l]) == l:
            print(t[i : i + l])
            if t[i : i + l] <= p:
                count = count + 1
        else:
            break
    return count
