def solution(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))

    if ab > ba:
        return ab
    else:
        return ba


def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))
