a, b = map(int, input().split())


def sol(a, b):
    if b > a:
        a, b = b, a
    
    while(b != 0):
        r = a%b
        a = b
        b = r
    return a

print(sol(a, b))
print(a*b // sol(a,b))