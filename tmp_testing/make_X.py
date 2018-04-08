# 1 3 5 6 7 8
import numpy as np
from sklearn import preprocessing

group_2 = ['R', 'M', 'L', 'A']

group_4 = ['PRAMIPEXOLE DIHYDROCHLORI', 'ROPINIROLE HCL', 'CARBIDOPA/LEVODOPA', 'NEUPRO', 'CARBIDOPA/LEVODOPA/ENTACA',
           'CARBIDOPA/LEVODOPA ER', 'MIRAPEX ER', 'ROPINIROLE ER', 'MIRAPEX', 'REQUIP', 'RYTARY', 'AZILECT',
           'CARBIDOPA/LEVODOPA ODT', 'ENTACAPONE', 'REQUIP XL', 'SINEMET', 'STALEVO 150', 'SINEMET CR', 'COMTAN',
           'STALEVO 50', 'STALEVO 100', 'STALEVO 125', 'STALEVO 75', 'STALEVO 200', 'PARCOPA']

group_10 = ['PUD', 'FP', 'DO', 'IM', 'NEUR', 'PED', '', 'PHA', 'NRP', 'SM', 'GER', 'PSY', 'DENT', 'RHU', 'PCC', 'GP',
            'OBG', 'MPD', 'OS', 'PM', 'NEPH', 'UROL', 'ANES', 'EM', 'CN', 'POD', 'PTH', 'SPM', 'PMD', 'ENDO', 'GS',
            'ID', 'PYG', 'ONC', 'CARD', 'NS', 'ND', 'THS', 'HEP', 'ALLR', 'GPM', 'CCM', 'GE', 'HEM', 'ADM', 'OTO',
            'ORS', 'HPM', 'CRS', 'VET', 'OM', 'OPH', 'OPT', 'OSS', 'PLS', 'PHR', 'UNSP', 'GEN', 'SURG', 'ALI', 'DERM',
            'CCS', 'NM', 'RAD', 'PA', 'NTR', 'PYA', 'CCP', 'CTS', 'CVS', 'DMP', 'OT', 'Y', 'MM', 'NA', 'N', 'NSP',
            'OCC']

tmp_1 = []
tmp_2 = []
tmp_3 = []

tmp_tmp = []
tmp_tmp_1 = []
tmp_tmp_2 = []
tmp_tmp_3 = []

with open("./data/testing/testing.csv") as f1:
    lines = f1.readlines()
    for line in lines:
        split = line.rstrip().split(",")
        if split[2] not in group_2:
            print line
        if split[4] not in group_4:
            print line
        if split[10] not in group_10:
            print line


# with open("./data/training/training.csv") as f1:
#     with open("./data/testing/testing.csv") as f2:
#         with open("./data/unknowndata/unknowndata.csv") as f3:
#             lines_1 = f1.readlines()
#             lines_2 = f2.readlines()
#             lines_3 = f3.readlines()
#
#             for line in lines_1:
#                 split = line.rstrip().split(",")
#                 line_tmp = []
#                 for i in [1, 3, 5, 6, 7, 8]:
#                     if split[i] != "":
#                         if i == 7:
#                             if len(split[i]) >= 5:
#                                 print line
#                                 line_tmp.append("10101010")
#                             else:
#                                 line_tmp.append(split[i])
#                         else:
#                             line_tmp.append(split[i])
#                     else:
#                         line_tmp.append("10101010")
#                 if len(line_tmp) == 6:
#                     line_tmp = map(float, line_tmp)
#                     # print line
#                     tmp_1.append(line_tmp)
#                 tmp_tmp.append([group_2.index(split[2]), group_4.index(split[4]), 0, group_10.index(split[10])])
#                 tmp_tmp_1.append([group_2.index(split[2]), group_4.index(split[4]), 0, group_10.index(split[10])])
#
#             for line in lines_2:
#                 split = line.rstrip().split(",")
#                 line_tmp = []
#                 for i in [1, 3, 5, 6, 7, 8]:
#                     if split[i] != "":
#                         if i == 7:
#                             if len(split[i]) >= 5:
#                                 line_tmp.append("10101010")
#                             else:
#                                 line_tmp.append(split[i])
#                         else:
#                             line_tmp.append(split[i])
#                     else:
#                         line_tmp.append("10101010")
#                 if len(line_tmp) == 6:
#                     line_tmp = map(float, line_tmp)
#                     # print line
#                     tmp_2.append(line_tmp)
#                 tmp_tmp.append([group_2.index(split[2]), group_4.index(split[4]), 0, group_10.index(split[10])])
#                 tmp_tmp_2.append([group_2.index(split[2]), group_4.index(split[4]), 0, group_10.index(split[10])])
#
#             for line in lines_3:
#                 split = line.rstrip().split(",")
#                 line_tmp = []
#                 for i in [1, 3, 5, 6, 7, 8]:
#                     if split[i] != "":
#                         if i == 7:
#                             if len(split[i]) >= 5:
#                                 line_tmp.append("10101010")
#                             else:
#                                 line_tmp.append(split[i])
#                         else:
#                             line_tmp.append(split[i])
#                     else:
#                         line_tmp.append("10101010")
#                 if len(line_tmp) == 6:
#                     line_tmp = map(float, line_tmp)
#                     # print line
#                     tmp_3.append(line_tmp)
#                 tmp_tmp.append([group_2.index(split[2]), group_4.index(split[4]), 0, group_10.index(split[10])])
#                 tmp_tmp_3.append([group_2.index(split[2]), group_4.index(split[4]), 0, group_10.index(split[10])])
#
#             enc = preprocessing.OneHotEncoder()
#             enc.fit(tmp_tmp)
#
#             pmt_1 = enc.transform(tmp_tmp_1).toarray()
#             pmt_2 = enc.transform(tmp_tmp_2).toarray()
#             pmt_3 = enc.transform(tmp_tmp_3).toarray()
#             # print pmt
#
#             result_1 = []
#             result_2 = []
#             result_3 = []
#
#             for i in range(len(tmp_1)):
#                 result_1.append(tmp_1[i] + pmt_1[i].astype(int).tolist())
#             result_1 = np.array(result_1)
#             print result_1.shape
#             np.savetxt("./data/training/X", result_1)
#
#             for i in range(len(tmp_2)):
#                 result_2.append(tmp_2[i] + pmt_2[i].astype(int).tolist())
#             result_2 = np.array(result_2)
#             print result_2.shape
#             np.savetxt("./data/testing/X", result_2)
#
#             for i in range(len(tmp_3)):
#                 result_3.append(tmp_3[i] + pmt_3[i].astype(int).tolist())
#             result_3 = np.array(result_3)
#             print result_3.shape
#             np.savetxt("./data/unknowndata/X", result_3)

