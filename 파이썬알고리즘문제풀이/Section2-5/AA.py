import sys

sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())

cnt = [0] * (n + k + 1)

for i in range(1, n + 1):
    for j in range(1, k + 1):
        cnt[i+j] += 1


max = 0
for i in range(n + k + 1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n + k + 1):
    if cnt[i] == max:
        print( i, end=' ')