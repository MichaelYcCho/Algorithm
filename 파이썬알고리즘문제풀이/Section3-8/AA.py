import sys

sys.stdin = open('input.txt', 'r')

line = int(input())
matrix = [list(map(int, input().split())) for _ in range(line)]

command = int(input())


for i in range(command):
    row, direction, count = map(int, input().split())
    for _ in range(count):
        if direction == 0:
            matrix[row - 1].append(matrix[row-1].pop(0))
        
        if direction == 1:
            matrix[row - 1].insert(0, matrix[row-1].pop())

answer = 0
start = 0
end = line
middle = line // 2

for i in range(line):
    for j in range(start, end):
        answer += matrix[i][j]
        
    if i < middle:
        start += 1
        end -= 1
    else:
        start -= 1
        end +=1


print(answer)
    


'''
import sys

sys.stdin = open('input.txt', 'r')

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

time = int(input())

for i in range(time):
   #row 행, direction 방향, num 개수
    row, direction, step = map(int, input().split())
    if direction == 0:
        for _ in range(step):
            #가장 앞의 값을 pop으로 뺀 후 뒤에 추가
            matrix[row-1].append(matrix[row -1].pop(0))
    else:
        for _ in range(step):
            #뒤에서 pop으로 꺼낸값을 가장 앞으로 insert함
            matrix[row-1].insert(0, matrix[row-1].pop())

        


res = 0
s = 0
e = n -1

for i in range(n):
    for j in range(s, e+1):
        res += matrix[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
    
print(res)









#order = [ list(map(int, input().split())) for _ in range(time)]

'''