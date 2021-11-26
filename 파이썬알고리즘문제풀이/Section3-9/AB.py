from pathlib import Path
import math

file_path = Path(__file__).parent / 'fourth_input.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    n = int()
    data = list()
    for index, line in enumerate(f):
        if index == 0:
            n = int(line.strip())
            data.append([0 for _ in range(n + 2)])
        else:
            line = f'0 {line} 0'
            data.append([int(integer_string.strip()) for integer_string in line.split(' ')])
    else:
        data.append([0 for _ in range(n + 2)])

count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        target = data[i][j]
        if target > data[i-1][j] and target > data[i][j-1] and target > data[i+1][j] and target > data[i][j+1]:
            count += 1
print(count)