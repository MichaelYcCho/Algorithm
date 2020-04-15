a = "123"
b = "12345"

#print(bool(a in b))


a = "가나다"
b = "가나다라"

print(bool(a in b))

'''
Q6588
n = int(input())
l = []
answer = []
answer2 = []

for i in range(2, n+1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else: l.append(i)


for i in range(n//2 +1):
    if i in l and n-i in l:
        answer.extend([[i, n-i]])     
        #print(f"{n} = {i} + {n-i}")

answer2.extend(answer[0])
print(f'{n} = {answer2[0]} + {answer2[1]}' )



#다른 route
num_list = []

while True:
    n = int(input())
    if n == 0:
        break
    num_list.append(n)

max_num = max(num_list)

sosu = [1 for i in range(max_num + 1)]
sosu[1] = 0
only_sosu = []

i = 2
while i <= max_num:
    print(f"i : {i}")
    if sosu[i] == 1:
        only_sosu.append(i)
        print(f"only_sosu : {only_sosu}")
        for j in range(i + i, max_num + 1, i):
            print(f"j {j}")
            print(i + i, max_num + 1, i)
            print(f"전 sosu{j} : {sosu[j]}")
            sosu[j] = 0
            print(f"후 sosu{j} : {sosu[j]}")
    i += 1

print(sosu)




'''



'''
a = 1000 - int(input())
b = [500, 100, 50, 10, 5, 1]
count = 0
for i in b:
    print(f"i : {i}")
    count += a // i
    print(f'count {count}')
    a %= i
    print(f'a = {a}')
print(count)
'''



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