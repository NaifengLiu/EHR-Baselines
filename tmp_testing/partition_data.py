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

    print float(rls) / float(len(y))
    print float(park) / float(len(y))
    print float(fibro) / float(len(y))


# RLS-PER-FOLD = 412,071
# PARK-PER-FOLD = 412,354
# FIBRO-PER-FOLD = 404,314


def partition(x_path, y_path):
    X = np.loadtxt(x_path)
    y = np.loadtxt(y_path)

    rls = []
    park = []
    fibro = []

    for i in range(len(y)):
        if int(y[i]) == 0:
            if len(rls) < 412071 * 8:
                rls.append(i)
        elif int(y[i]) == 1:
            if len(park) < 412354 * 8:
                park.append(i)
        elif int(y[i]) == 2:
            if len(fibro) < 404314:
                fibro.append(i)

    for i in range(8):
        # # rls
        # tmp = rls[i * 412071: (i + 1) * 412071]
        # tmp_save = X[tmp, :]
        # print tmp_save.shape
        # np.savetxt("./data/training/rls_" + str(i), tmp_save)
        # # park
        # tmp = park[i * 412354: (i + 1) * 412354]
        # tmp_save = X[tmp, :]
        # print tmp_save.shape
        # np.savetxt("./data/training/park_" + str(i), tmp_save)
        # fibro
        tmp = fibro[i * 50539: (i + 1) * 50539]
        tmp_save = X[tmp, :]
        print tmp_save.shape
        np.savetxt("./data/training/fibro_" + str(i), tmp_save)


partition("./data/training/X", "./data/training/y")
