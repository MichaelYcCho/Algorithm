import sys

N = int(input())

stack = []

for i in range(N):
    k = sys.stdin.readline().split()
    if(k[0] == 'push'):
        stack.append(int(k[1]))
    elif(k[0] == 'pop'):
        if not stack:
            print('-1')
        else:
            print(stack.pop(-1))
    elif(k[0] == 'size'):
        print(len(stack))
    elif(k[0] == 'empty'):
        if not stack:
            print('1')
        else:
            print('0')
    elif(k[0] == 'top'):
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])

    

