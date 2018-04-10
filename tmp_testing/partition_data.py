import numpy as np


def count(file_path):
    rls = 0
    park = 0
    fibro = 0
    y = np.loadtxt(file_path)
    for i in range(len(y)):
        if int(y[i]) == 0:
            rls += 1
        elif int(y[i]) == 1:
            park += 1
        elif int(y[i]) == 2:
            fibro += 1

    print rls
    print park
    print fibro

    print float(rls)/float(len(y))
    print float(park)/float(len(y))
    print float(fibro)/float(len(y))




