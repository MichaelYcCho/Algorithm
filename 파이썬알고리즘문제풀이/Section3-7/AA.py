# 사과나무

import sys

sys.stdin = open('input.txt', 'r')

n = int(input())

a = [list(map(int, input().split())) for _ in range(n) ]

answer = 0




start = end = middle = int(n//2)
for i in range(n):
    for j in range(start, end+1):
        answer += a[i][j]
    
    if i < middle:
        start -=1
        end +=1
    else:
        start += 1
        end -= 1 

       

print(answer)














'''
import sys

sys.stdin = open('input.txt', 'r')

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

res = 0
# s = start, e = end
s = e = n // 2
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)
379
'''