import numpy as np

group_0 = []
group_1 = []
group_2 = []
group_3 = []
group_4 = []
group_5 = []
group_6 = []
group_7 = []
group = [[],[],[],[],[],[],[],[]]


with open("./data/test.csv") as f:
    for lines in f.readlines():
        split = lines.rstrip().split(",")
        for i in range(8):
            if split[i] not in group[i]:
                group[i].append(split[i])

for sub_group in group:
    print sub_group
