import numpy as np

l = np.zeros((5, 4), dtype=int)
ll = np.full((7, 6), 2, dtype=int)
ll[1:6, 1:5] = l

'''
l[0] = 2
l[-1] = 2


for i in l:
    i[0] = 2
    i[-1] = 2
'''

print(ll) 