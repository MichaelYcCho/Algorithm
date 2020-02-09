# 대문자 소문자 변환
s = input()
result = []

for i in s:
    if i.islower():
        result.append(i.upper())
    else:
        result.append(i.lower())

print(''.join(result))

'''
for i in result:
    print(i, end= "")
'''
