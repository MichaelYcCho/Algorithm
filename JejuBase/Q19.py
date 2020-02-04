# Q19 
# 공백으로 숫자 2개를 받고 a와 b를 승의 관계로 출력 

'''
# 방법 1
user_input = input()
l = user_input.split(' ')
a = int(l[0])
b = int(l[1])

print(a**b)
'''

# 방법 2

user_input = input()
l = user_input.split(' ')
changel = []

for i in l:
    changel.append(int(i))
print(changel[0]**changel[1])
