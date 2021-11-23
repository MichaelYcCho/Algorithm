number_list = [
    [10, 13, 10, 12, 15],
    [12, 39, 30, 28, 11],
    [11, 25, 50, 53, 15],
    [19, 27, 29, 37, 27],
    [19, 13, 30, 13, 19]
]

result = list()
n = len(number_list[0])

for row in number_list:
    result.append(sum(row))

for i in range(n):
    col = list()
    for j in range(n):
        col.append(number_list[j][i])
    result.append(sum(col))

positive_diagonal = list()
for i in range(n):
    positive_diagonal.append(number_list[i][i])
result.append(sum(positive_diagonal))

negative_diagonal = list()
for i in reversed(range(n)):
    negative_diagonal.append(number_list[i][i])
result.append(sum(negative_diagonal))

print(max(result))