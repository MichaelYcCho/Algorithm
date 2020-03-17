n = int(input())

for i in range(n):
    text = input().split()
    for j in text:
        print(j[::-1], end=' ')
    print()


