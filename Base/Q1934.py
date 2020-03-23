def sol(a, b):
    r = 0
    if b > a:
        a, b = b, a
    
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a



n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(a * b // sol(a, b))