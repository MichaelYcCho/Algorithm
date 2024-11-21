def solution(l, r):
    answer = []
    for i in range(l, r+1):
        check = True
        for s in str(i):
            if s != "5" and s != "0":
                check = False
                break
        if check == True:
            answer.append(i)
        
    if  not answer:
        return [-1]
    return answer;


def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    return answer if answer else [-1]