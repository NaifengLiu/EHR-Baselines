import numpy as np

tmp = np.loadtxt("./result/5_fold_result/sum/sum")

row = np.sum(tmp, axis=0)

tmp = []
tmp.append([row[3], row[7], row[8], row[1], row[5], row[0], row[4], row[2], row[6]])

print tmp



