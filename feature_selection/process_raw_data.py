import numpy as np
import csv

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

tmp = []
tmp_tmp = []

b = [0, 3, 5, 6, 7, 8, 9]
c = [2, 4, 10]
d = [11]

with open("./data/diag_grp_1M_10.csv", "rb") as f:
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
        print i
