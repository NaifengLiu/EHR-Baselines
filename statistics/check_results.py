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

    print true_num+false_num
    print np.loadtxt(address).shape



check_file("503")
check_file("203")
