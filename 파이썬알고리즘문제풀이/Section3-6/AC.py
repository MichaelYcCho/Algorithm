number_list = [
    [10, 13, 10, 12, 15],
    [12, 39, 30, 28, 11],
    [11, 25, 50, 53, 15],
    [19, 27, 29, 37, 27],
    [19, 13, 30, 13, 19]
]

result = list()
n = len(number_list[0])

positive_diagonal = list()
negative_diagonal = list()
for i in range(n):
    row = number_list[i]
    result.append(sum(row))

    positive_diagonal.append(number_list[i][i])

    negative_index = n-1-i
    negative_diagonal.append(number_list[negative_index][negative_index])

    col = list()
    for j in range(n):
        col.append(number_list[j][i])

    result.append(sum(col))

result.append(sum(positive_diagonal))
result.append(sum(negative_diagonal))

print(max(result))