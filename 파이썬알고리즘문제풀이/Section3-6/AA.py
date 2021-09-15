import sys

sys.stdin = open('input.txt', 'r')
n = int(input())

# map은 한줄을 읽어서 list해서 저장
# 이것을 n번 돌면서 list로 계속 저장함 이중리스트로 저장됨
a = [list(map(int, input().split())) for _ in range(n)]

#print(a) #[[10, 13, 10, 12, 15], [12, 39, 30, 23, 11], [11, 25, 50, 53, 15], [19, 27, 29, 37, 27], [19, 13, 30, 13, 19]]

# 행(row_sum)과 열(column_sum)의합

largest = -2147000000
for i in range(n):
    row_sum = column_sum = 0
    for j in range(n):
        row_sum += a[i][j] # i번째 행의 합
        column_sum += a[j][i] # j번째 열의 합

    if row_sum > largest:
        largest = row_sum

    if column_sum > largest:
        largest = column_sum

sum1 = sum2 = 0
for i in range(n): # n이 5일때
    sum1 += a[i][i] # (0, 0), (1, 1), (2, 2) ... 의 합
    sum2 += a[i][n-i-1] # (0, 4), (1, 3), (2, 2) ... 의 합
    
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)