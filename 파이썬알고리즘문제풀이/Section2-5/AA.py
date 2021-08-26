import sys

#sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())

cnt_list = [0] * (n + k + 1)
result = []

for i in range(1, n + 1):
    for j in range(1, k + 1):
        cnt_list[i + j] += 1

max_count = max(cnt_list)

for idx, cnt in enumerate(cnt_list):
    if cnt == max_count:
        result.append(idx)
        print(idx, end=' ')

'''
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
'''