import numpy as np
result_group = ['RLS\n', 'PARK\n', 'FIBRO\n']

y = []

with open("./data/testing/testing.csv", "w+") as w:
    for i in range(1, 4):
        with open("./data/testing/"+str(i)+".csv") as f:
            f.readline()
            for line in f.readlines():
                split = line.split(",")
                y.append(result_group.index(split[-1]))

y = np.array(y)

print y.shape

np.savetxt("./data/testing/y", y)



