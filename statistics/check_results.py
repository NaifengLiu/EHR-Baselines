import numpy as np
import os


def check_supervised_file(address, method):
    times = int(float(address[0:2]))
    nn = int(float(address[2]))

    print times
    print nn

    hae_folder_path = "./data/person/hae"
    non_hae_folder_path = "./data/person/nonhae"

    hae_file_names = os.listdir(hae_folder_path)
    hae_file_names_length = len(hae_file_names)

    non_hae_file_names = os.listdir(non_hae_folder_path)[0:1233 * times]
    non_hae_file_names_length = len(non_hae_file_names)

    true_num = len(hae_file_names[int(hae_file_names_length * 0.8):hae_file_names_length])
    false_num = len(non_hae_file_names[int(non_hae_file_names_length * 0.8):non_hae_file_names_length])

    result = np.loadtxt(address+method)

    recall = 0
    for i in range(true_num):
        if result[i] == 1:
            recall += 1

    print "method: " + method
    print "times = " + str(times) + ", knn parameter = " + str(nn)
    print "precision: " + str(float(recall) / float(np.sum(result)))
    print "recall: " + str(float(recall) / float(true_num))


# check_supervised_file("501", "l1")
# check_supervised_file("502", "l1")
# check_supervised_file("503", "l1")
# check_supervised_file("504", "l1")
# check_supervised_file("505", "l1")
#
# check_supervised_file("501", "euclidean")
# check_supervised_file("502", "euclidean")
# check_supervised_file("503", "euclidean")
# check_supervised_file("504", "euclidean")
# check_supervised_file("505", "euclidean")


def check_unsupervised_file(address, method):
    tmp = np.loadtxt(address + method + "_U")
    num = int(float(address[2]))
    count = 0
    for i in range(1233):
        for j in range(num):
            item = tmp[i][j]
            if item < 1233:
                count += 1
    print address + method
    print float(count-1233)/(float(1233)*float(num-1))


# check_unsupervised_file("501", "l1")
# check_unsupervised_file("502", "l1")
# check_unsupervised_file("503", "l1")
# check_unsupervised_file("504", "l1")
# check_unsupervised_file("505", "l1")
# check_unsupervised_file("502", "euclidean")
# check_unsupervised_file("503", "euclidean")
# check_unsupervised_file("504", "euclidean")
# check_unsupervised_file("505", "euclidean")


def check_unsupervised_precision_recall(address, method):
    tmp = np.loadtxt(address + method + "_U")
    num = int(float(address[2]))
    count = 0
    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0
    for i in range(len(tmp)):
        this = 0
        for j in range(1, num):
            item = tmp[i][j]
            print item
            if item < 1233:
                this += 1
        if this >= (num-1)/2+1:
            if i < 1233:
                true_positive += 1
            elif i >= 1233:
                false_positive += 1
        else:
            if i < 1233:
                false_negative += 1
            else:
                true_negative += 1
    print true_positive
    print true_negative
    print false_positive
    print false_negative
    print "p: " + str(float(true_positive) / (float(true_positive) + float(false_positive)))
    print "r: " + str(float(true_positive) / (float(true_positive) + float(false_negative)))


check_unsupervised_precision_recall("502", "l1")
