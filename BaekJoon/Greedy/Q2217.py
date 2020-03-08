N = int(input())
rope = []
high = []

for i in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)
for j in range(N):
    high.append(rope[j]*(j+1))

print(max(high))