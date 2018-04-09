import numpy as np

test_labels = np.loadtxt("./data/testing/result_labels")

y = np.loadtxt("./data/testing/y")

cell_00 = 0
cell_01 = 0
cell_02 = 0
cell_10 = 0
cell_11 = 0
cell_12 = 0
cell_20 = 0
cell_21 = 0
cell_22 = 0

for i in range(len(y)):
    if int(y[i]) == 0:
        if int(test_labels) == 0:
            cell_00 += 1
        elif int(test_labels) == 1:
            cell_01 += 1
        elif int(test_labels) == 2:
            cell_02 += 1
    elif int(y[i]) == 1:
        if int(test_labels) == 0:
            cell_10 += 1
        elif int(test_labels) == 1:
            cell_11 += 1
        elif int(test_labels) == 2:
            cell_12 += 1
    elif int(y[i]) == 2:
        if int(test_labels) == 0:
            cell_20 += 1
        elif int(test_labels) == 1:
            cell_21 += 1
        elif int(test_labels) == 2:
            cell_22 += 1

print cell_00
print cell_01
print cell_02
print cell_10
print cell_11
print cell_12
print cell_20
print cell_21
print cell_22

