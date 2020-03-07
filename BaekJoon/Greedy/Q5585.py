
def sol(Okane):
    coin = [500, 100, 50, 10, 5, 1]
    num = 0
    for i in range(len(coin)):
        if coin[i] <= Okane:
            mok = Okane // coin[i]
            Okane -= coin[i]*mok
            num += mok
    return num



N = 1000 - int(input())

print(sol(N))


'''
a = 1000 - int(input())
b = [500, 100, 50, 10, 5, 1]
count = 0
for i in b:
    count += a // i
    a %= i
print(count)

'''

