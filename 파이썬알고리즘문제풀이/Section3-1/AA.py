import sys

sys.stdin = open('input.txt', 'r')
n = int(input())

for i in range(n):
    char = input().upper()
    #print(char)
    size = len(char) // 2

    #print(char[:size])
   # print(char[::-1][:size])
    #아래를 더 간단하게
    if char == char[::-1]:
        print(f'{i + 1} Yes')
    else:
        print(f'{i + 1} NO') 


'''
    # 맨 뒤부터 출력 :size길이까지 
    if char[:size] == char[::-1][:size]:
        print('YES')
    else:
        print('NO')
'''

'''
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[size-1-j]:
            print(f'{i + 1} NO')
            break
    else:
        print(f'{i + 1} NO')
'''