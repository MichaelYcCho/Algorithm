import sys

sys.stdin = open('input.txt', 'r')

n = int(input())
score_list = list(map(int, input().split()))

cnt = 0
result = 0

for i in score_list:
    if i == 1:
        cnt += 1
        result += cnt
    else:
        cnt = 0

print(result)