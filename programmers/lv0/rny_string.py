def solution(rny_string):
    return rny_string.replace("m", "rn")


def solution(rny_string):
    answer = []
    for x in rny_string:
        if x == "m":
            answer.append("rn")
        else:
            answer.append(x)
    return "".join(answer)
