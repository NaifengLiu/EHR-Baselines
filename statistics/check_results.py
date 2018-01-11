import numpy as np
import os


def check_file(address):
    times = int(float(address[0:2]))
    nn = int(float(address[-1]))

    hae_folder_path = "./data/person/hae"
    non_hae_folder_path = "./data/person/nonhae"

    hae_file_names = os.listdir(hae_folder_path)
    hae_file_names_length = len(hae_file_names)

    non_hae_file_names = os.listdir(non_hae_folder_path)[0:1233 * times]
    non_hae_file_names_length = len(non_hae_file_names)

    true_num = len(hae_file_names[int(hae_file_names_length * 0.8):hae_file_names_length])
    false_num = len(non_hae_file_names[int(non_hae_file_names_length * 0.8):non_hae_file_names_length])

    result = np.loadtxt(address)

    recall = 0
    for i in range(true_num):
        if result[i] == 1:
            recall += 1

    print "times = " + str(times) + ", knn parameter = " + str(nn)
    print "precision: " + str(float(recall) / float(np.sum(result)))
    print "recall: " + str(float(recall) / float(true_num))


check_file("201")
check_file("202")
check_file("203")
check_file("204")
check_file("205")
check_file("501")
check_file("502")
check_file("503")
check_file("504")
check_file("505")
