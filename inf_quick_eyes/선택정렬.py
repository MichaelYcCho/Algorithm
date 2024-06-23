# O(n^2)

input_list = [5, 10, 66, 77, 54, 32, 11, 15]
sorted_list = []


while input_list:
    sorted_list.append(min(input_list))
    input_list.pop(input_list.index(min(input_list)))
print(sorted_list)
