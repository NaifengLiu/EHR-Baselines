import numpy as np
from sklearn import preprocessing

patient = dict()
group_1 = ['ROPINIROLE HCL', 'CARBIDOPA/LEVODOPA', 'PRAMIPEXOLE DIHYDROCHLORI', 'ROPINIROLE ER',
           'CARBIDOPA/LEVODOPA ER', 'REQUIP XL', 'REQUIP', 'NEUPRO', 'ENTACAPONE', 'CARBIDOPA/LEVODOPA ODT',
           'MIRAPEX ER', 'MIRAPEX', 'RYTARY', 'CARBIDOPA/LEVODOPA/ENTACA', 'AZILECT', 'SINEMET', 'SINEMET CR',
           'STALEVO 75', 'STALEVO 200', 'STALEVO 150', 'STALEVO 125', 'STALEVO 100', 'COMTAN', 'STALEVO 50', 'PARCOPA']

group_2 = ['R', 'M', 'L', 'A']

group_3 = ['FP', 'DO', 'NRP', 'NEUR', 'IM', 'MPD', 'PUD', 'PHA', 'GER', 'RHU', 'PCC', 'PMD', 'CARD', 'NS', 'CN', 'PSY',
           'SM', 'OBG', 'ANES', 'SPM', '', 'GS', 'OS', 'GP', 'ONC', 'PM', 'NEPH', 'ALLR', 'PED', 'ID', 'OPH', 'EM',
           'POD', 'ENDO', 'GE', 'UROL', 'ORS', 'THS', 'OTO', 'HEM', 'RAD', 'NM', 'PYG', 'CCM', 'OPT', 'DENT', 'SURG',
           'GPM', 'UNSP', 'HPM', 'OM', 'PLS', 'PYA', 'NTR', 'DERM', 'ND', 'PTH', 'DMP', 'VET', 'ADM', 'OSS', 'GEN',
           'PHR', 'HEP', 'PA', 'CCS', 'OT', 'CCP', 'CTS', 'MM', 'CRS']

result_group = ['RLS\n', 'PARK\n', 'FIBRO\n']

tmp = []

tmptmp = []

result_tmp = []

with open("diag_grp_1M.csv") as f:
    f.readline()
    for line in f.readlines():
        line_split = line.split(",")
        if line_split[7] != '':
            tmp_1 = [line_split[1], line_split[0], line_split[3], line_split[5], line_split[6], line_split[7]]
        else:
            tmp_1 = [line_split[1], line_split[0], line_split[3], line_split[5], line_split[6], '10101010']

        tmp_1 = map(int, tmp_1)
        tmp.append(tmp_1)

        tmp_2 = [group_2.index(line_split[2]), group_1.index(line_split[4]), group_3.index(line_split[8])]
        tmptmp.append(tmp_2)

        result_tmp.append(result_group.index(line_split[9]))

result_tmp = np.array(result_tmp)

# np.savetxt("y", result_tmp)

print result_tmp[558888]
print result_tmp[999999]

# print tmp
#
# enc = preprocessing.OneHotEncoder()
# enc.fit(tmptmp)
#
# pmt = enc.transform(tmptmp).toarray()
# print pmt
#
# result = []
#
# for i in range(len(tmp)):
#     result.append(tmp[i] + pmt[i].astype(int).tolist())
#
# result = np.array(result).astype(int)
# np.savetxt("result", result)
