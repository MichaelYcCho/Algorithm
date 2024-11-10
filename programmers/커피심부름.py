def solution(order):
    answer = 0

    for s in order:
        if s == "anything" or "americano" in s:
            answer += 4500
        elif "cafelatte" in s:
            answer += 5000

    return answer


def solution(order):
    answer = 0
    for i in order:
        if i in [
            "iceamericano",
            "americanoice",
            "hotamericano",
            "americanohot",
            "americano",
            "anything",
        ]:
            answer += 4500
        else:
            answer += 5000
    return answer
