# 10진수 2진수로

a = int(input())
b = []

while a:
    b.append(str(a % 2))
    a = int(a / 2)
    
b.reverse()
print(int(''.join(b)))
