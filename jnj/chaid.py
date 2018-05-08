import numpy as np

for i in range(5):
    tmp_0 = np.loadtxt("./result/5_fold_result/sum/0")
    tmp_1 = np.loadtxt("./result/5_fold_result/sum/1")
    tmp_2 = np.loadtxt("./result/5_fold_result/sum/2")
    tmp_3 = np.loadtxt("./result/5_fold_result/sum/3")
    tmp_4 = np.loadtxt("./result/5_fold_result/sum/4")
    tmp = (tmp_0 + tmp_1 + tmp_2 + tmp_3 + tmp_4) / 5

row = np.sum(tmp, axis=0)

tmp = []
tmp.append([row[3], row[7], row[8], row[1], row[5], row[0], row[4], row[2], row[6]])

print tmp



