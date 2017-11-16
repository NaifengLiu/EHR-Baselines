import numpy as np

patients_info = dict()

rx_dx = [22, 23, 24, 25, 26, 27, 28, 29, 30]

with open("data/combined_data") as f:
    for line in f:
        line_split = line.rstrip().split(",")
        patients_info[int(float(line_split[0]))] = []
        for i in range(1, len(line_split)):
            if i - 1 in rx_dx:
                patients_info[int(float(line_split[0]))].append(float(line_split[i]))

print len(patients_info[29508505])
print len(patients_info[133311493])
print patients_info[133311493]
