def solution(rsp):
    result = {"2": "0", "0": "5", "5": "2"}
    answer = ""
    for i in rsp:
        answer += result.get(i)
    return answer


def solution(rsp):
    rsp = rsp.replace("2", "s")
    rsp = rsp.replace("5", "p")
    rsp = rsp.replace("0", "r")
    rsp = rsp.replace("r", "5")
    rsp = rsp.replace("s", "0")
    rsp = rsp.replace("p", "2")
    return rsp
