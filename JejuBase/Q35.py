# 제곱하는 팩토리얼 함수  함수 구현

def one(n):
    def two(value):
        return value ** n
    return two


a = one(2) # 2제곱
b = one(3)


print(a(10)) # 즉 100이 출력되어야함 
print(b(10))

'''
a = one(2) 이므로 2를 받음 
이때 one함수는 two를 리턴함
즉 a 가 two함수가 된다고 보는것 
즉 a는 n이 2인 two함수를 받는 것임 

'''