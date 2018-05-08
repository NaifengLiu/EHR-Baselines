import numpy as np

tmp = np.loadtxt("./result/y_result_prob")

row = np.sum(tmp, axis=0)

tmp = []
tmp.append([row[3], row[7], row[8], row[1], row[5], row[0], row[4], row[2], row[6]])


