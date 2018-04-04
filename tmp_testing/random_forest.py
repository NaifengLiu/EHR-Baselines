import numpy as np

patient = dict()
group = []

with open("diag_grp_1M.csv") as f:
    f.readline()
    for line in f.readlines():
        line_split = line.split(",")
        # print line_split[7]
        if line_split[4] not in group:
            group.append(line_split[4])

print group
