import random as r

# chr 해당 숫자에 해당하는 아스키코드로 변환해줌 

l = [chr(i) for i in range(65, 91)]
#print(l)
total_medicine = []
medicine = []


'''
for i in range(8):
    medicine.append(r.choice(l))

'''

for i in range(100):
    total_medicine.append(r.sample(l, 8))
#print(total_medicine)


user_input = input().split(' ')
#user_input[1] = int(user_input[1])
#print(user_input)
result = []

for i in total_medicine:
    if len(set(i) & set(user_input[0])) == int(user_input[1]):
        result.append(i)

print(len(result))