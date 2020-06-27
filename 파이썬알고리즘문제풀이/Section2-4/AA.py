import sys

sys.stdin = open("input.txt", "r")

n = int(input())

k = list(map(int, input().split()))


min = 2147000000
avg = int((sum(k) /n)+ 0.5)

for idx, x in enumerate(k):
    tmp = abs(x - avg)
    if tmp < min:
        min = tmp
        score = x
        studentNo = idx +1

    elif tmp == min:
        if x > score:
            score = studentNo = idx + 1


print(score, studentNo)
   