def solution(numbers, direction):
    if direction == "right":
        numbers.insert(0, numbers.pop())
    else:
        numbers.append(numbers.pop(0))
    return numbers


def solution(numbers, direction):
    if direction == "right":
        numbers.insert(0, numbers[-1])
        numbers.pop()
        return numbers
    else:
        numbers.append(numbers[0])
        numbers.pop(0)
        return numbers


from collections import deque


def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == "right":
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)
