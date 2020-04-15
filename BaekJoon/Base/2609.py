a, b = map(int, input().split())


def sol(a, b):
    if b > a:
        a, b = b, a
    
    while(b != 0):
        r = a%b
        print(f'r : {r}')
        a = b
        print(f'a : {a}')
        b = r
        print(f'b : {b}')
        print("============= \n")
    return a

print(sol(a, b))
print(a*b // sol(a,b))