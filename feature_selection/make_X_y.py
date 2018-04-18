import numpy as np
from sklearn import preprocessing
import csv

default = 0

with open("./data/diag_grp_1M_10.csv", "rb") as f:
    f.readline()
    reader = csv.reader(f)
    for line in reader:
        split = line
        if len(split) != default:
            default = len(split)
            print default

