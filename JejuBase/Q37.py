l = input().split()
count = 0
for i in range(1, len(l)):
    if l.count(l[i-1]) < l.count(l[i]):
        count = i

print(count)
print(l[count])

print('{}이가 {}표로 반장이 되었습니다.'.format(l[count], l.count(l[count])))


# 이때 i는 가장 많이 카운팅된 인덱스를 출력함



