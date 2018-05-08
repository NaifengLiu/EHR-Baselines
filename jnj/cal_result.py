import numpy as np
#           0              1           2       3       4         5           6           7        8
# ['ISCHEMIC_STROKE', 'CAD_ONLY', 'CAD_ACS', 'ACS', 'AFIB', 'PAD_ONLY', 'ALL_OTHER', 'PAD_ACS', 'CHF']

# y_result = np.loadtxt("./result/y_result")
# y_truth = np.loadtxt("./data/y_test")
#
# right = 0
# wrong = 0
#
# matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
#
# for i in range(len(y_truth)):
#     matrix[int(y_truth[i])][int(y_result[i])] += 1
#
# print matrix

# result = [[1415, 37910, 4, 588, 1671, 45, 19773, 0, 0],
#           [865, 163266, 119, 2795, 5055, 29, 32949, 0, 0],
#           [90, 40325, 161, 1087, 622, 17, 4169, 1, 0],
#           [808, 31568, 146, 5491, 619, 12, 6404, 0, 0],
#           [53, 13294, 1, 84, 6680, 0, 14404, 0, 0],
#           [607, 33519, 12, 453, 1553, 36, 20806, 0, 1],
#           [713, 50383, 32, 949, 3693, 30, 78220, 0, 0],
#           [4, 977, 0, 23, 49, 0, 359, 1, 0],
#           [84, 7656, 8, 108, 1642, 2, 8757, 0, 2]]
#
# tmp = []
#
# for row in result:
#     tmp.append([row[3], row[7], row[8], row[1], row[5], row[0], row[4], row[2], row[6]])
#
# print tmp

# for i in range(5):
#     tmp_0 = np.loadtxt("./result/5_fold_result/"+str(i)+"_0")
#     tmp_1 = np.loadtxt("./result/5_fold_result/"+str(i)+"_1")
#     tmp_2 = np.loadtxt("./result/5_fold_result/"+str(i)+"_2")
#     tmp_3 = np.loadtxt("./result/5_fold_result/"+str(i)+"_3")
#     tmp_4 = np.loadtxt("./result/5_fold_result/"+str(i)+"_4")
#     tmp_5 = np.loadtxt("./result/5_fold_result/"+str(i)+"_5")
#     tmp_6 = np.loadtxt("./result/5_fold_result/"+str(i)+"_6")
#     tmp_7 = np.loadtxt("./result/5_fold_result/"+str(i)+"_7")
#     tmp_8 = np.loadtxt("./result/5_fold_result/"+str(i)+"_8")
#     tmp_9 = np.loadtxt("./result/5_fold_result/"+str(i)+"_9")
#     tmp_10 = np.loadtxt("./result/5_fold_result/"+str(i)+"_10")
#     tmp_11 = np.loadtxt("./result/5_fold_result/"+str(i)+"_11")
#     tmp = (tmp_0 + tmp_1 + tmp_2 + tmp_3 + tmp_4 + tmp_5 + tmp_6 + tmp_7 + tmp_8 + tmp_9 + tmp_10 + tmp_11) / 12
#     print tmp.shape
#     np.savetxt("./result/5_fold_result/"+str(i), tmp)


# for i in range(5):
#     tmp_0 = np.loadtxt("./result/5_fold_result/sum/0")
#     tmp_1 = np.loadtxt("./result/5_fold_result/sum/1")
#     tmp_2 = np.loadtxt("./result/5_fold_result/sum/2")
#     tmp_3 = np.loadtxt("./result/5_fold_result/sum/3")
#     tmp_4 = np.loadtxt("./result/5_fold_result/sum/4")
#     tmp = (tmp_0 + tmp_1 + tmp_2 + tmp_3 + tmp_4) / 5
#     np.savetxt("./result/5_fold_result/sum/sum", tmp.argmax(axis=1))

    