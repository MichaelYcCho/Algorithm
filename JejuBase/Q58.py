# , 찍기

# 방법 1 재귀함수

def comma(n):
    if len(n) < 3:
        return n
    else:
        return comma(n[:len(n)-3]) + ',' + n[len(n)-3:]

print(comma('10000000'))

# 방법2 format() 활용
print(format(10000000, ','))
