import numpy as np

a = [[1, 2, 3], [4, 5, 6]]

b = [[3, 2, 1], [6, 5, 4]]

c = [[5, 5, 5]]

d = np.concatenate((a, b, c, e), axis=0)

print d

for i in range(8):
    for j in range(8):
        rls = (a, b, c)
