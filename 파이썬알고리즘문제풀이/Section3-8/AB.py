from pathlib import Path
import math

file_path = Path(__file__).parent / 'third_input.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    raw_data = f.readlines()

    n = int(raw_data[0].strip())
    data = [list(map(int, raw_string.strip().split(' '))) for raw_string in raw_data[1:1 + n]]
    m = int(raw_data[1 + n])
    commends = [list(map(int, raw_string.strip().split(' '))) for raw_string in raw_data[2+n:2+n+m]]

for commend in commends:
    target_row = data[commend[0] - 1]
    is_right = commend[1]
    cnt = commend[2]

    if is_right:
        for _ in range(cnt):
            target = target_row.pop(n-1)
            target_row.insert(0, target)
    else:
        for _ in range(cnt):
            target = target_row.pop(0)
            target_row.append(target)


'''
for commend in commends:
    target_row = data[commend[0] - 1]
    is_right = commend[1]
    cnt = commend[2]

    loop = cnt % 5

    if is_right:
        data[commend[0] - 1] = target_row[-loop:] + target_row[:-loop]
    else:
        data[commend[0] - 1] = target_row[loop:] + target_row[:loop]
'''

base_index = math.trunc(n / 2)
result = data[base_index][base_index]
index = 0
while True:
    row1 = data[index]
    row2 = data[n - 1 - index]
    result += sum(row1[0+index:n-index])
    result += sum(row2[0+index:n-index])
    index += 1
    if index == base_index:
        break

print(result)