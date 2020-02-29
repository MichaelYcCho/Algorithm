
'''
# 방법 1
value = """0 1 0 0 0 
    0 0 0 0 0
    0 0 0 1 0
    0 0 1 0 0
    0 0 0 0 0 """

value = value.replace('1', 'f')
l = [i.strip() for i in value.split('\n')]
l = [i.split(' ') for i in l]
count = 0  # 상, 하에 부여하기위한 변수 
#print(l)


for i in l:
    for j in i:
        if j == 'f':
            if i.index(j) > 0:
                i[i.index(j)-1] = '*'
            if i.index(j) < 4:
                i[i.index(j)+1] = '*'
    if count > 0:
        l[count-1][i.index(j)] = '*'
    if count <4:
        l[count+1][i.index(j)] = '*'
    count += 1

print(l)

'''

# 방법 2
# 이차원배열을 일차원배열로 치환하여

value = '''0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0'''
value = value.replace('1', 'f')
print(value)

l = value.split(' ')
for i in range(len(l)):
    if l[i] == 'f':
        #print(i)
        if i % 5 != 0:
            l[i-1] = '*'
        if i % 5 != 4:
            l[i+1] = '*'
        if i // 5 != 0:
            l[i-5] = '*'
        if i // 5 != 4:
            l[i+5] = '*'


print(l)


print(l[0:5])
print(l[5:10])
print(l[10:15])
print(l[15:20])
print(l[20:25])