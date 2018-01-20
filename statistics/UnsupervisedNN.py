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

    print "entering hae patients"
    print str(datetime.now())

    for item in hae_file_names[0:int(hae_file_names_length)]:
        X.append(np.loadtxt(hae_folder_path + "/" + item))

    print "entering non hae patients"
    print str(datetime.now())

    for item in non_hae_file_names[0:int(non_hae_file_names_length)]:
        X.append(np.loadtxt(non_hae_folder_path + "/" + item))

    print "start training"
    print str(datetime.now())

    nbrs = NearestNeighbors(n_neighbors=b, algorithm='auto', metric=metric).fit(X)

    print "saving result"
    print str(datetime.now())
    distances, indices = nbrs.kneighbors(X)
    np.savetxt(str(a) + str(b) + metric + "_U", indices)


# run(50, 1, 'euclidean')
# run(50, 2, 'euclidean')
# run(50, 3, 'euclidean')
# run(50, 4, 'euclidean')
# run(50, 5, 'euclidean')

# run(50, 1, 'l1')
# run(50, 2, 'l1')
# run(50, 3, 'l1')
# run(50, 4, 'l1')
run(50, 5, 'l1')
