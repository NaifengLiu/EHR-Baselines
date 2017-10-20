import numpy as np
patients_info = dict()

with open("data/combined_data") as f:
    for line in f:
        line_split = line.rstrip().split(",")
        patients_info[int(float(line_split[0]))] = []
        for i in range(1, len(line_split)):
            patients_info[int(float(line_split[0]))].append(float(line_split[i]))


# print patients_info[596215486]


