from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import os
from datetime import datetime

print "loading folder"

hae_folder_path = "./data/person/hae"
non_hae_folder_path = "./data/person/nonhae"

hae_file_names = os.listdir(hae_folder_path)
hae_file_names_length = len(hae_file_names)

non_hae_file_names = os.listdir(non_hae_folder_path)[0:1233*50]
non_hae_file_names_length = len(non_hae_file_names)

print "start generating matrix"
print str(datetime.now())

X = []
y = []

print "entering hae patients"
print str(datetime.now())

for item in hae_file_names[0:int(hae_file_names_length*0.8)]:
    X.append(np.loadtxt(hae_folder_path+"/"+item))
    y.append(1)

print "entering non hae patients"
print str(datetime.now())

for item in non_hae_file_names[0:int(non_hae_file_names_length*0.8)]:
    X.append(np.loadtxt(non_hae_folder_path+"/"+item))
    y.append(0)

print "start training"
print str(datetime.now())

neigh = KNeighborsClassifier(n_neighbors=1)
neigh.fit(X, y)

print "preparing testing data"
print str(datetime.now())

test_X = []

for item in hae_file_names[int(hae_file_names_length*0.8):hae_file_names_length]:
    test_X.append(np.loadtxt(hae_folder_path+"/"+item))
for item in non_hae_file_names[int(non_hae_file_names_length*0.8):non_hae_file_names_length]:
    test_X.append(np.loadtxt(non_hae_folder_path+"/"+item))

print "predicting"
print str(datetime.now())

test_y = neigh.predict(test_X)

print "saving results"
print str(datetime.now())

np.savetxt("501", test_y)
