# 숫자 input으로 받으면 역순으로 출력되게

user_input = input()
l = list(user_input.split())
l = [int(i) for i in l]
# print(l[::-1])
for i in range (len(l) , 0, -1):
    print(i, end= " ")