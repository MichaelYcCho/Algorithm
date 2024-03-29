def solution(money):
    price = 5500
    return [money // price, money % price]


def solution(money):
    # 두 숫자를 나누어 몫과 나머지를 tuple로 반환
    return divmod(money, 5500)
