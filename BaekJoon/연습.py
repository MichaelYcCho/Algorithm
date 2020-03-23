
a = 1000 - int(input())
b = [500, 100, 50, 10, 5, 1]
count = 0
for i in b:
    count += a // i
    print(f'count {count}')
    a %= i
    print(f'a = {a}')
print(count)




'''
n = input().split()
print(n[0])


stk = []
stk.append(1)
stk.append(2)
stk.pop(-1)
print(stk)
'''


'''
N = int(input())
user_input = input().split()
user_input2 = input()

print(user_input)
print(user_input2)
print(user_input2[0])
'''
'''
stack = []

for i in range(N):
    if(user_input[0] == 'push'):
        stack.append(int(user_input[1]))
    elif(user_input[0] == 'pop'):
        pass

'''