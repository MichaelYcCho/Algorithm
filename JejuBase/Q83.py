def math(e):
    m = {
        ')':'(',
        '}':'{', 
    }

    stack = []
    for i in e:
        if i in '({':
            stack.append(i)
            #만약 len이 0인데 i가 m이라는 것은 닫는괄호가 먼저나왔다는 것이므로 false
        elif i in m:
            if len(stack) == 0:
                return False
            # 괄호가 (} 같이 맞지 않는 경우
            else: 
                t = m[i]
                if t != stack.pop():
                    return False
    return len(stack) == 0
           


while 1:
    order = input('데이터입력 : (1), 프로그램종료 : (2)')
    if order == '1':
        ex = input('데이터를 입력하세요 : ')
        print(math(ex))
    else:
        break



    '''
def math(e):
    m = {
        ')':'(',
        '}':'{', 
    }

    stack = []
    print(stack)

    for i in e:
        if i in '({':
            stack.append(i)
            print(stack)    
        else:
            print('없음')    


math('{(')



--------------------------

def math(e):
    m = {
        ')':'(',
        '}':'{', 
    }

    stack = []

    for i in e:
        if i in '({':
            stack.append(i)
        elif i in m:
            if len(stack) == 0:
                return False
            else: 
                print(f'i는 {i}')
                print(f'm[i] : {m[i]}')
                t = m[i]
                print(f't {t}')
                if t != stack.pop():
                    return False
    return len(stack) == 0



print(math('{()}'))


    '''