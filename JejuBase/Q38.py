l = input().split()
l = [int(i) for i in l]
count = 0

for i in range(3):
    top = max(l)
    count += l.count(top)
    for j in range(l.count(top)):
        l.remove(top)
print(count)