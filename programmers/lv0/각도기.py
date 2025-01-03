def solution(angle):
    if 0 < angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 90 < angle < 180:
        answer = 3
    elif angle == 180:
        answer = 4
    else:
        print("error")
    return answer


def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer
