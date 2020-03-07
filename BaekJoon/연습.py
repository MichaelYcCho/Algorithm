#InputArr.sort(key=lambda x: (x[1], x[0]))

x = [[2, 3], [1, 2]]
b = sorted(x, key=lambda x: x[1])

print(b)