import sys

#sys.stdin = open("input.txt", "r")

n = int(input())
student_score = list(map(int, input().split()))

avarage = round(sum(student_score) / n)


min_gap = 1000
min_idx = 1000
score = 0

for idx, x in enumerate(student_score):
    abs_num = abs(avarage - x)

    if abs_num < min_gap:
        min_gap = abs_num
        score = x
        min_idx = idx

    elif min_gap == abs_num:
        if x > score:
            score = x
            min_idx = idx

print(avarage, min_idx+1)




'''
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
            studentNo = idx + 1


print(score, studentNo)
'''