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

tmp = []

tmp_tmp = []

with open("./data/training/training.csv") as f:
    lines = f.readlines()

    for line in lines:
        split = line.rstrip().split(",")
        line_tmp = []
        for i in [1, 3, 5, 6, 7, 8]:
            if split[i] != "":
                if i == 7:
                    if len(split[i]) >= 5:
                        line_tmp.append("10101010")
                else:
                    line_tmp.append(split[i])
            else:
                line_tmp.append("10101010")
        if len(line_tmp) == 6:
            line_tmp = map(float, line_tmp)
            # print line
            tmp.append(line_tmp)

        tmp_tmp.append([group_2.index(split[2]), group_4.index(split[4]), 0, group_10.index(split[10])])

    enc = preprocessing.OneHotEncoder()
    enc.fit(tmp_tmp)

    pmt = enc.transform(tmp_tmp).toarray()
    # print pmt

    result = []

    for i in range(len(tmp)):
        result.append(tmp[i] + pmt[i].astype(int).tolist())

    # print result

    result = np.array(result)

    print result.shape

    np.savetxt("X", result)

