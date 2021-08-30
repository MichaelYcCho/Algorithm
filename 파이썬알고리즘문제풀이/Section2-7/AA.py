import sys

n = int(input())

ch = [True] * (n + 1)
result = []

for i in range(2, n+1):
    if ch[i]:
        result.append(i)
        for j in range(i, n+1, i):
            ch[j] = False


print(len(result))
print(*result, sep = ', ')


'''
sys.stdin= open("input.txt", "r")

n = int(input())
ch = [0]*(n+1) #21

cnt = 0

for i in range(2, n+1):
    if ch[i] == 0:
        cnt +=1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)
'''

