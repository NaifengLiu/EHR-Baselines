import numpy as np
import csv

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open("./data/diag_grp_1M_10.csv", "rb") as f:
    f.readline()
    reader = csv.reader(f)
    for line in reader:
        split = line
        for i in range(len(split)):
            print split[i]
            print split[i][0]
            if str(split[i][0]).isalpha():
                a[i] = 1

print a
