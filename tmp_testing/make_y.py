import numpy as np
result_group = ['RLS\n', 'PARK\n', 'FIBRO\n']

y = []

with open("./data/training/training.csv", "w+") as w:
    for i in range(1, 8):
        with open("./data/training/"+str(i)+".csv") as f:
            f.readline()
            for line in f.readlines():
                split = line.split(",")
                y.append(result_group.index(split[-1]))

y = np.array(y)

print y.shape

np.savetxt("./data/training/y", y)



