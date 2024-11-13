def solution(myString):
    tmp = myString.split("x")
    return [len(i) for i in tmp]


def solution(myString):
    answer = []
    myString = myString.split("x")
    for i in myString:
        answer.append(len(i))
    return answer
