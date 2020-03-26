l = []

for i in range(9):
    l.append(int(input()))

sum_l = sum(l)

spyA = 0
spyB = 0 

for i in range(8):
    for j in range(i+1, 9):
        if sum_l - (l[i] + l[j]) == 100:
            spyA = l[i]
            spyB = l[j]
l.remove(spyA)
l.remove(spyB)
l.sort()


for i in l:
    print(i)
