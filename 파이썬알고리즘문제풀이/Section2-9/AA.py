import sys

sys.stdin = open("input.txt", "rt")


n = int(input())
reward = 0


for i in range(n):
    a, b, c = map(int, input().split())
    
    if a == b == c:
        reward = max(reward, 10000 + (a * 1000))
    elif a == b or a == c:
        reward = max(reward, 1000 + (a * 100))
    elif b == c:
        reward = max(reward, 1000 + (b * 100))
    else:
        reward = max(reward, max(a, b, c) * 100)

print(reward)





