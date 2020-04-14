def solution(v):
    answer = []
    v1 = []
    v2 = []
    for i in v:
        if i[0] not in v1:
            v1.append(i[0])
        else:
            v1.remove(i[0])
        if i[1] not in v2:
            v2.append(i[1])
        else:
            v2.remove(i[1])
    answer = v1 + v2
    return answer


v = [[1, 4], [3, 4], [3, 10]]
v2 = [[1, 1], [2, 2], [1, 2]]
 
print(solution(v2))