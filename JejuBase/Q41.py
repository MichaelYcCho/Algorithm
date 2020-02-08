x = int(input())
ch = True

for i in range(2, x):
    if x % i == 0:
        ch = False

if ch == True:
    print("소수")
else:
    print("소수 아님")


