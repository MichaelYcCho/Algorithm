# 문자열압축

user_input = input()
s = ''
count = 1
strStore = user_input[0]

for i in user_input:
    if i == strStore:
        count += 1
    else:
        s += str(count) + strStore
        strStore = i
        count = 1
        
s += str(count) + strStore
print(s)


