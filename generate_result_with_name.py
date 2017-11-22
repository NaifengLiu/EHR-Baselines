import grouping
import load_patient_info
import numpy as np
from tqdm import tqdm
from sklearn.ensemble import RandomForestClassifier

matching = grouping.matching
matching_keys = matching.keys()
#######################################################################################################################
x_train_file_names_positive = []
x_test_file_names_positive = []

for i in range(len(matching_keys)):
    if len(x_train_file_names_positive) < 985:
        x_train_file_names_positive.append(matching_keys[i])
    else:
        x_test_file_names_positive.append((matching_keys[i]))

test = []
for patient in x_test_file_names_positive:
    test.append(patient)
for patient in x_test_file_names_positive:
    for non_patient in matching[patient]:
        test.append(non_patient)

v_result = np.zeros(248*201)
for i in range(5):
    v_result += np.loadtxt("result/bagging_random_forest/fold_"+str(i+1)+"_test").astype(float)

for item in v_result:
    print item
