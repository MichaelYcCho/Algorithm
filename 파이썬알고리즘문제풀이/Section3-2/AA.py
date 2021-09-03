import sys

sys.stdin = open('input.txt', 'r')

#isdigit은 숫자형태는 모두 찾아줌
s = input()
res = 0
cnt = 0

for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)

for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1

print(res, cnt)


''' 나의 풀이 '''
'''

n = input()

number_list = []
cnt = 0


for i in n:
    if i.isnumeric():
        number_list.append(i)

new_number = int(''.join(number_list))


for i in range(1, new_number + 1):
    if new_number % i == 0:
        cnt += 1

print(new_number,  cnt)
'''