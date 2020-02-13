# 두 리스트 번갈아가면서 출력

a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']

c = []
count = 0 # 홀짝에 따라서 먼저 추가할 리스트를 구분하기위한 변수

for i, j in zip(a, b):
    if count % 2 == 0:
        c.append([i, j])
    else:
        c.append([j, i])
    count += 1

print(c)