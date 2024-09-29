def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    elif dot[0] > 0 and dot[1] < 0:
        return 4


# True = 1, False = 0 || [0][0]:3사분면, [0][1]:2사분면, [1][0]:4사분면, [1][1]:1사분면
def solution(dot):
    quad = [(3, 2), (4, 1)]
    # quad = [(2, 1), (3, 4)]; return quad[dot[1]<0][dot[0]>0]
    return quad[dot[0] > 0][dot[1] > 0]


# https://school.programmers.co.kr/learn/courses/30/lessons/120841
