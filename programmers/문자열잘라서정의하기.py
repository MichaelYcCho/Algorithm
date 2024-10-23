def solution(myString):
    return sorted(i for i in myString.split("x") if i)


def solution(myString):
    a = []
    for x in myString.split("x"):
        if x:
            a.append(x)
    return sorted(a)
