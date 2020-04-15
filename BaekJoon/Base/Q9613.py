import sys

def sol(a,b):
    while b != 0:
        a, b = b, a % b
    return a


n = int(sys.stdin.readline())

for _ in range(n):
    l = list(map(int, input().split()))
    total = 0
    count = len(l)


    for i in range(1, count-1):
        for j in range(i + 1, count):
            total += sol(l[i], l[j])
            print(total)
        print("=============")
    print(total)


'''
문제를 잘 읽을 것
l에서의 첫번째수는 테스트케이스의 숫자이다. (인수가 아님!)

'''