from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import os

hae_folder_path = "./data/person/hae"
non_hae_folder_path = "./data/person/nonhae"

hae_file_names = os.listdir(hae_folder_path)
hae_file_names_length = len(hae_file_names)

non_hae_file_names = os.listdir(non_hae_folder_path)
non_hae_file_names_length = len(non_hae_file_names)

X = []
y = []

for item in hae_file_names[0:int(hae_file_names_length*0.8)]:
    X.append(np.loadtxt(hae_folder_path+"/"+item))
    y.append(1)
for item in non_hae_file_names[0:int(non_hae_file_names_length*0.8)]:
    X.append(np.loadtxt(non_hae_folder_path+"/"+item))
    y.append(0)

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)

test_X = []

for item in hae_file_names[int(hae_file_names_length*0.8):hae_file_names_length]:
    test_X.append(np.loadtxt(hae_folder_path+"/"+item))
for item in non_hae_file_names[int(non_hae_file_names_length*0.8):non_hae_file_names_length]:
    test_X.append(np.loadtxt(non_hae_folder_path+"/"+item))

print neigh.predict(test_X)
