import sys

sys.stdin = open('input.txt', 'r') # Read input from input.txt file

n = int(input()) # Number of test cases
a = list(map(int, input().split()))
m = int(input()) # Number of operations
b = list(map(int, input().split()))


result_list = []



while(True):
    if len(a) == 0:
        result_list += b
        break
    if len(b) == 0:
        result_list += a
        break

    if len(a) > 0 and  len(b) > 0:
        if a[0] >= b[0]:
            result_list.append(b.pop(0))
        elif a[0] <= b[0]:
            result_list.append(a.pop(0))

print(*result_list, sep=' ')
'''

p1 = p2 = 0
c = []

while p1<n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
    
if p1 < n:
    c += a[p1:]
if p2 < m:
    c += b[p2:]

for x in c:
    print(x, end=' ')
'''