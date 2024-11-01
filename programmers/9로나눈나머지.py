def solution(number):
    # 각 자리 숫자의 합을 저장할 변수 sum
    sum = 0

    for num in str(number):
        sum += int(num)

    answer = sum % 9
    return answer


def solution(number):
    n = 0
    for x in number:
        n += int(x)
    return n % 9


def solution(number):
    answer = 0

    for x in number:
        answer += int(x)
    answer = answer % 9

    return answer
