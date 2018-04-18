import numpy as np
import csv

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

group_1 = []
group_4 = []
group_6 = []
group_13 = []
group_16 = []
group_17 = []
group_29 = []
group_44 = []
group_45 = []
group_46 = []
group_47 = []
group_48 = []

tmp = []
tmp_tmp = []

b = [0, 2, 3, 5, 7, 8, 9, 10, 11, 12, 14, 15, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36,
     37, 38, 39, 40, 41, 42, 43]
c = [1, 4, 6, 13, 16, 17, 29, 44, 45, 46, 47, 48]
d = [49]

with open("./data/diag_grp_1M_48.csv", "rb") as f:
    f.readline()
    reader = csv.reader(f)
    for line in reader:
        split = line
        if split[1] not in group_1:
            group_1.append(split[1])
        if split[4] not in group_4:
            group_4.append(split[4])
        if split[6] not in group_6:
            group_6.append(split[6])
        if split[13] not in group_13:
            group_13.append(split[13])
        if split[16] not in group_16:
            group_16.append(split[16])
        if split[17] not in group_17:
            group_17.append(split[17])
        if split[29] not in group_29:
            group_29.append(split[29])
        if split[44] not in group_44:
            group_44.append(split[44])
        if split[45] not in group_45:
            group_45.append(split[45])
        if split[46] not in group_46:
            group_46.append(split[46])
        if split[47] not in group_47:
            group_47.append(split[47])
        if split[48] not in group_48:
            group_48.append(split[48])
print ""
print group_1
print ""
print group_4
print ""
print group_6
print ""
print group_13
print ""
print group_16
print ""
print group_17
print ""
print group_29
print ""
print group_44
print ""
print group_45
print ""
print group_46
print ""
print group_47
print ""
print group_48