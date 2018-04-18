import numpy as np
import csv

a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

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

tmp = []
tmp_tmp = []

b = []
c = []
d = [11]

with open("./data/diag_grp_1M_48.csv", "rb") as f:
    f.readline()
    reader = csv.reader(f)
    for line in reader:
        split = line
        for i in range(len(split)):
            if split[i] == "":
                continue
            else:
                if str(split[i][0]).isalpha():
                    a[i] = 1

for i in range(len(a)):
    if a[i] != 0:
        b.append(i)
    else:
        c.append(i)

print b
print c

