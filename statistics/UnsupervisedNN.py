from sklearn.neighbors import NearestNeighbors
import numpy as np
import os
from datetime import datetime


def run(a, b, metric):
    print "loading folder"

    hae_folder_path = "./data/person/hae"
    non_hae_folder_path = "./data/person/nonhae"

    hae_file_names = os.listdir(hae_folder_path)
    hae_file_names_length = len(hae_file_names)

    non_hae_file_names = os.listdir(non_hae_folder_path)[0:1233 * a]
    non_hae_file_names_length = len(non_hae_file_names)

    print "start generating matrix"
    print str(datetime.now())

    X = []
    new_X = []

    print "entering hae patients"
    print str(datetime.now())

    for item in hae_file_names[0:int(hae_file_names_length)]:
        X.append(np.loadtxt(hae_folder_path + "/" + item))
        new_X.append(np.loadtxt(hae_folder_path + "/" + item))

    print "entering non hae patients"
    print str(datetime.now())

    for item in non_hae_file_names[0:int(non_hae_file_names_length)]:
        X.append(np.loadtxt(non_hae_folder_path + "/" + item))

    print "start fitting"
    print str(datetime.now())

    nbrs = NearestNeighbors(n_neighbors=b, algorithm='auto', metric=metric).fit(X)

    print "calculating result"
    print str(datetime.now())
    distances, indices = nbrs.kneighbors(new_X)
    # np.savetxt(str(a) + str(b) + metric + "_U", indices)

    print "finishing"
    tmp = indices
    num = b
    count = 0
    for i in range(1233):
        for j in range(num):
            item = tmp[i][j]
            if item < 1233:
                count += 1
    print str(a) + str(b) + metric
    rate = float(count - 1233) / (float(1233) * float(num - 1))
    print float(count - 1233) / (float(1233) * float(num - 1))
    with open(str(a) + str(b) + metric + "result", "w+") as w:
        w.write(str(rate))
        w.close()


# run(200, 1, 'euclidean')
run(200, 2, 'euclidean')
# run(200, 3, 'euclidean')
# run(200, 4, 'euclidean')
# run(200, 5, 'euclidean')
# run(200, 6, 'euclidean')

# run(200, 1, 'l1')
# run(200, 2, 'l1')
# run(200, 3, 'l1')
# run(200, 4, 'l1')
# run(200, 5, 'l1')
# run(200, 6, 'l1')
