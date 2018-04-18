import numpy as np
import csv
from sklearn import preprocessing

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

group_2 = ['R', 'M', 'L', 'A']
group_4 = ['ROPINIROLE HCL', 'CARBIDOPA/LEVODOPA', 'PRAMIPEXOLE DIHYDROCHLORI', 'ROPINIROLE ER',
           'CARBIDOPA/LEVODOPA ER', 'REQUIP XL', 'REQUIP', 'NEUPRO', 'ENTACAPONE', 'CARBIDOPA/LEVODOPA ODT',
           'MIRAPEX ER', 'MIRAPEX', 'RYTARY', 'CARBIDOPA/LEVODOPA/ENTACA', 'AZILECT', 'SINEMET', 'SINEMET CR',
           'STALEVO 75', 'STALEVO 200', 'STALEVO 150', 'STALEVO 125', 'STALEVO 100', 'COMTAN', 'STALEVO 50', 'PARCOPA']
group_10 = ['FP', 'DO', 'NRP', 'NEUR', 'IM', 'MPD', 'PUD', 'PHA', 'GER', 'RHU', 'PCC', 'PMD', 'CARD', 'NS', 'CN', 'PSY',
            'SM', 'OBG', 'ANES', 'SPM', '', 'GS', 'OS', 'GP', 'ONC', 'PM', 'NEPH', 'ALLR', 'PED', 'ID', 'OPH', 'EM',
            'POD', 'ENDO', 'GE', 'UROL', 'ORS', 'THS', 'OTO', 'HEM', 'RAD', 'NM', 'PYG', 'CCM', 'OPT', 'DENT', 'SURG',
            'GPM', 'UNSP', 'HPM', 'OM', 'PLS', 'PYA', 'NTR', 'DERM', 'ND', 'PTH', 'DMP', 'VET', 'ADM', 'OSS', 'GEN',
            'PHR', 'HEP', 'PA', 'CCS', 'OT', 'CCP', 'CTS', 'MM', 'CRS']

y_group = ['RLS', 'PARK', 'FIBRO']

tmp = []
tmp_tmp = []
y_tmp = []

b = [0, 3, 5, 6, 7, 8, 9]
c = [2, 4, 10]
d = [11]

with open("./data/diag_grp_1M_10.csv", "rb") as f:
    f.readline()
    reader = csv.reader(f)
    for line in reader:
        split = line
        line_tmp = []
        for i in b:
            if split[i] == "":
                split[i] = "10101010"
            line_tmp.append(split[i])
        if len(line_tmp) == 7:
            line_tmp = map(float, line_tmp)
            tmp.append(line_tmp)
        tmp_tmp.append([group_2.index(split[2]), group_4.index(split[4]), 0, group_10.index(split[10])])
        y_tmp.append(y_group.index(split[11]))
    enc = preprocessing.OneHotEncoder()
    enc.fit(tmp_tmp)

    pmt = enc.transform(tmp_tmp).toarray()
    result = []

    for i in range(len(tmp)):
        result.append(tmp[i] + pmt[i].astype(int).tolist())
    result = np.array(result)
    print result.shape
    y_tmp = np.array(y_tmp)
    np.savetxt("./data/X", result)
    np.savetxt("./data/y", y_tmp)

