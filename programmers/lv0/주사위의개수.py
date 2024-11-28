def solution(box, n):
    return int(box[0] // n) * int(box[1] // n) * int(box[2] // n)


def solution(box, n):
    x, y, z = box
    return (x // n) * (y // n) * (z // n)
