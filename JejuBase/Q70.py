import numpy as np

a = [[1, 2], [3, 4]]

'''
# Case1 numpy 활용

a = np.array(a)
#print(a)
#print(a * 2)
#print(a * a)

a = np.asmatrix(a)
#print(a)
#print(a * 2)
#print(a * a)
'''

# Case2 

a = [[1, 2], [3, 4]]
b = [[1, 2], [3, 4]]
c = []

# c의 총 행은 a의 length 만큼
for i in range(len(a)):
    # 행의 요소는 b[0]만큼 해당문제의 경우 b[0] = [1, 2]이므로 2개 
    c.append([0] * len(b[0]))
print(c)

for i in range(len(c)):
    for j in range(len(c[i])):  
        for k in range(len(a[i])):
            c[i][j] += a[i][k] * b[k][j]

print(c)