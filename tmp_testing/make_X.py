# 1 3 5 6 7 8
import numpy as np
from sklearn import preprocessing

tmp = []

tmp_tmp = []

# with open("./data/training/X.csv", "w+") as w:
#     with open("./data/training/training.csv") as f:
#         lines = f.readlines()
#
#         q = 0
#
#         for line in lines:
#             split = line.rstrip().split(",")
#             line_tmp = []
#             for i in [1, 3, 5, 6, 7, 8]:
#                 if split[i] != "":
#                     line_tmp.append(split[i])
#                 else:
#                     line_tmp.append("10101010")
#             if len(line_tmp) == 6:
#                 tmp.append(line_tmp)
#
#             tmp_tmp.append([split[2], split[4], 0, split[10]])
#
#             q += 1
#
#             if q >= 10:
#                 break
#
#         enc = preprocessing.OneHotEncoder()
#         enc.fit(tmp_tmp)
#
#         pmt = enc.transform(tmp_tmp).toarray()
#         print pmt
#
#         result = []
#
#         for i in range(len(tmp)):
#             result.append(tmp[i] + pmt[i].astype(int).tolist())
#
#         print result
#
#         # result = np.array(result).astype(int)
#         # np.savetxt("result", result)

group_2 = []
group_4 = []
group_10 = []

with open("./data/training/training.csv") as f_1:
    with open("./data/testing/testing.csv") as f_2:
        with open("./data/unknowndata/unknowndata.csv") as f_3:
            lines_1 = f_1.readlines()
            lines_2 = f_2.readlines()
            lines_3 = f_3.readlines()

            for line in lines_1:
                split = line.rstrip().split(",")
                if split[2] not in group_2:
                    group_2.append(split[2])

            for line in lines_2:
                split = line.rstrip().split(",")
                if split[2] not in group_2:
                    group_2.append(split[2])

            for line in lines_3:
                split = line.rstrip().split(",")
                if split[2] not in group_2:
                    group_2.append(split[2])

            for line in lines_1:
                split = line.rstrip().split(",")
                if split[4] not in group_4:
                    group_4.append(split[4])

            for line in lines_2:
                split = line.rstrip().split(",")
                if split[4] not in group_4:
                    group_4.append(split[4])

            for line in lines_3:
                split = line.rstrip().split(",")
                if split[4] not in group_4:
                    group_4.append(split[4])

            for line in lines_1:
                split = line.rstrip().split(",")
                if split[10] not in group_10:
                    group_10.append(split[10])

            for line in lines_2:
                split = line.rstrip().split(",")
                if split[10] not in group_10:
                    group_10.append(split[10])

            for line in lines_3:
                split = line.rstrip().split(",")
                if split[10] not in group_10:
                    group_10.append(split[10])

print group_2
print ""
print group_4
print ""
print group_10

