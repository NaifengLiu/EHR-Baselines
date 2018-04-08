import numpy as np
result_group = ['RLS\n', 'PARK\n', 'FIBRO\n']

y = []

with open("./data/training/training.csv") as f:
    lines = f.readlines()
    for line in lines:
        split = line.split(",")
        y.append(split[-1])

y = np.array(y)

print y.shape

np.savetxt("./data/training/y", y)


