import numpy as np

# ['ISCHEMIC_STROKE', 'CAD_ONLY', 'CAD_ACS', 'ACS', 'AFIB', 'PAD_ONLY', 'ALL_OTHER', 'PAD_ACS', 'CHF']

y_result = np.loadtxt("./result/y_result")
y_truth = np.loadtxt("./data/y_test")

right = 0
wrong = 0

matrix = np.array((9, 9))

for i in range(len(y_truth)):
    matrix[y_truth[i]][y_result[i]] += 1

print matrix
