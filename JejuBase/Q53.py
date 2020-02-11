#괄호 짝맞춤

def 괄호체크(s):
    if s.count('(') != s.count(')'):
        return 'NO'
    괄호 = []
    for i in s:
        if i == '(':
            괄호.append('(')
        if i == ')':
            if len(괄호) == 0:   # len이 0이라는것은 닫기괄호가 먼저들어왔거나 열기괄호가 생성되기 전 이라는 뜻 
                                # 괄호의 시작은 항상 '(' 로 시작하기때문에 )가 먼저 들어올 수있는 경우는 0여야함 
                return 'NO'
            괄호.pop() # 결과적으로 ')' 이면 '('가 pop되면서 괄호변수는 빈 리스트가됨 결과적으로 빈리스트가된다면 짝이 맞다는 것이므로 YES
            print(f" 괄호: {괄호}")
    return 'YES'

user_input = input()
print(괄호체크(user_input))