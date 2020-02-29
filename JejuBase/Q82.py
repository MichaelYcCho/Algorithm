def math(e):
    count = 0
    for i in e:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
    if count == 0:
        return True
    else:
        return False


while 1:
    order = input('데이터입력 : (1), 프로그램종료 : (2)')
    if order == '1':
        ex = input('데이터를 입력하세요 : ')
        print(math(ex))
    else:
        break