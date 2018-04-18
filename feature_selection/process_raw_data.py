import numpy as np
import csv

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

group_2 = []
group_4 = []
group_10 = []

with open("./data/diag_grp_1M_10.csv", "rb") as f:
    f.readline()
    reader = csv.reader(f)
    for line in reader:
        split = line
        if split[2] not in group_2:
            group_2.append(split[2])
        if split[4] not in group_4:
            group_4.append(split[4])
        if split[10] not in group_10:
            group_10.append(split[10])

print group_2
print group_4
print group_10
