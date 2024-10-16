def solution(order):
    answer = 0
    for i in str(order):
        if i in ["3", "6", "9"]:
            answer += 1
    return answer


def solution(order):
    answer = 0
    order = str(order)
    return order.count("3") + order.count("6") + order.count("9")
