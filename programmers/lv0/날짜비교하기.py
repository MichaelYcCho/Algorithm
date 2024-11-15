def solution(date1, date2):
    answer = 0
    if date1[0] < date2[0]:
        return 1
    elif date1[0] > date2[0]:
        return 0
    else:
        if date1[1] < date2[1]:
            return 1
        elif date1[1] > date2[1]:
            return 0
        else:
            if date1[2] < date2[2]:
                return 1
            else:
                return 0
    return answer


def solution(date1, date2):
    for i in range(3):
        if date1[i] < date2[i]:
            return 1
        elif date2[i] < date1[i]:
            return 0
    return 0
