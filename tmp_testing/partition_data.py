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
            rls.append(i)
        elif int(y[i]) == 1:
            park.append(i)
        elif int(y[i]) == 2:
            fibro.append(i)

    for i in range(8):
        this_fold_rls_validation = rls[i * (len(rls) / 8):(i + 1) * (len(rls) / 8)]
        this_fold_rls_train = [item for item in rls if item not in this_fold_rls_validation]
        this_fold_park_validation = park[i * (len(park) / 8):(i + 1) * (len(park) / 8)]
        this_fold_park_train = [item for item in park if item not in this_fold_park_validation]
        this_fold_fibro_validation = fibro[i * (len(fibro) / 8):(i + 1) * (len(fibro) / 8)]
        this_fold_fibro_train = [item for item in fibro if item not in this_fold_fibro_validation]
        for j in range(8):
            undersampling_rls = this_fold_rls_train[
                                j * (len(this_fold_rls_train) / 8):(j + 1) * (len(this_fold_rls_train) / 8)]
            undersampling_park = this_fold_park_train[
                                 j * (len(this_fold_park_train) / 8):(j + 1) * (len(this_fold_park_train) / 8)]
            undersampling_fibro = this_fold_fibro_train

            print len(this_fold_rls_validation)
            print len(this_fold_park_validation)
            print len(this_fold_fibro_validation)
            print len(undersampling_rls)
            print len(undersampling_park)
            print len(undersampling_fibro)

            undersampling = undersampling_rls + undersampling_park + undersampling_fibro
            this_X = X[undersampling, :]
            this_y = np.concatenate((len(undersampling_rls), len(undersampling_park), len(undersampling_fibro)), axis=0)
            np.savetxt(str(i)+str(j)+"_X", this_X)
            np.savetxt(str(i)+str(j)+"_y", this_y)

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
        # tmp = fibro[i * 50539: (i + 1) * 50539]
        # tmp_save = X[tmp, :]
        # print tmp_save.shape
        # np.savetxt("./data/training/fibro_" + str(i), tmp_save)


partition("./data/training/X", "./data/training/y")
