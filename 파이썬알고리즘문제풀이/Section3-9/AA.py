import sys

sys.stdin = open('input.txt', 'r')

n = int(input())
origin_matrix = [list(map(int, input().split())) for _ in range(n)]


answer_matrix = [[0 for _ in range(n +2)] for _ in range(n + 2)]


for i in range(n):
    for j in range(n):
        answer_matrix[i+1][j+1] = origin_matrix[i][j]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0 , -1]

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all( answer_matrix[i][j] > answer_matrix[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1



print(cnt)

'''

import sys

sys.stdin = open('input.txt', 'r')

n = int(input())

matrix = [list(map(int, input().split())) for _  in range(n)]


m = [[0] * (n+2) for _ in range(n+2)]



for i in range(n):
    for j in range(n):
        m[i+1][j+1] = matrix[i][j]
        
print(m)        
        
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


cnt =0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(m[i][j] > m[i + dx[k]] [j + dy[k]]  for k in range(4)):
            cnt +=1


print(cnt)
'''




'''
import sys
sys.stdin=open("input.txt","rt")
 
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
 
# [0] 값을 가장자리에 돌림
m=[[0]*(n+2) for _ in range(n+2)]
print(m)

for x in range(n):
    for y in range(n):
        if x<n+2 and y<n+2:
            m[x+1][y+1]=a[x][y]
 
res=0
 
# 상하좌우 비교하는 로직
for x in range(n+2):
    for y in range(n+2):
        if 0<x<n+1 and 0<y<n+1:
            # 자기자신을 제외한 max_num
            max_num=max(m[x][y-1],m[x][y+1],m[x-1][y],m[x+1][y])
            # 자기 자신이 상하좌우 값의 최댓값보다 크다면
            if m[x][y]>max_num:
                res+=1
 
print(res)
'''



'''
import sys
sys.stdin = open('input.txt', 'r')

# dx dy 를 조합하면 각각 한칸 위 우 아래 좌를 의미
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 0번째 행에 [0]*n 개의 값을 넣는다. 즉 최상단을 0으로 채움
a.insert(0, [0] * n)

# 최하단 행에 [0]*n 개의 값을 넣는다. 즉 최하단을 0으로 채움
a.append([0] * n)

#각 행의 첫번째와 마지막 index에 0을 추가하여 완성
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n + 1 ):
        #if all은 all안의 모든 조건이 참일때만 참
        if all(a[i][j] > a[i+ dx[k]][j+ dy[k]] for k in range(4)):
            cnt += 1

print(cnt)
'''