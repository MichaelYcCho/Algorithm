# 2번 문제
from pathlib import Path
import math

file_path = Path(__file__).parent / 'input.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    n = int()
    data = list()
    for index, line in enumerate(f):
        if index == 0:
            n = int(line.strip())
        else:
            data.append([int(integer_string.strip()) for integer_string in line.split(' ')])

base_index = math.trunc(n / 2)

result = sum(data[base_index])

index = 0
while True:
    row1 = data[index]
    row2 = data[n - 1 - index]
    result += sum(row1[base_index - index: base_index + 1 + index])
    result += sum(row2[base_index - index: base_index + 1 + index])

    index += 1
    if index == base_index:
        break

print(result)