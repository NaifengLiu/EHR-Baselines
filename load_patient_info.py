import numpy as np

patients_info = dict()

rx_dx = [0, 1, 2, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231,
         232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247]

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
