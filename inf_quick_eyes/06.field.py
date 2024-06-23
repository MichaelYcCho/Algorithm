field1 = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
]

field2 = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 3],
    [0, 0, 0, 0, 4],
    [0, 2, 0, 0, 2],
    [4, 5, 0, 2, 0],
]


import numpy as np

# 시계 방향으로 원하면 -1
array_sum = np.rot90(field2, 1) + np.array(field1)
result = chr(int("".join([str(i) for i in array_sum[0]]), 8))

for k in range(5):
    print(chr(int("".join([str(i) for i in array_sum[k]]), 8)))
