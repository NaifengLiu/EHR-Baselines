import grouping
import load_patient_info
import numpy as np
from tqdm import tqdm
from sklearn.ensemble import RandomForestClassifier
import random

matching = grouping.matching
matching_keys = matching.keys()
patients_info = load_patient_info.patients_info
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
    test.append(patients_info[patient])
for patient in x_test_file_names_positive:
    for non_patient in matching[patient]:
        test.append(patients_info[non_patient])
test = np.array(test)

#######################################################################################################################
negative_list = []
for item in x_train_file_names_positive:
    for one in matching_keys[item]:
        negative_list.append(one)

random.shuffle(negative_list)

for fold_num in range(5):
    print("start " + str(fold_num + 1) + " fold")
    tmp_validation_names_positive = x_train_file_names_positive[fold_num * 197:(fold_num + 1) * 197]
    tmp_training_names_positive = \
        [item for item in x_train_file_names_positive if item not in tmp_validation_names_positive]

    validation_X = []
    for patient in tmp_validation_names_positive:
        validation_X.append(patients_info[patient])
    for patient in tmp_validation_names_positive:
        for non_patient in matching[patient]:
            validation_X.append(patients_info[non_patient])

    this_fold_test_result = np.zeros(len(test))
    this_fold_validation_result = np.zeros(197 * 201)

    for j in tqdm(range(200)):
        X = []
        for item in tmp_training_names_positive:
            X.append(patients_info[item])
        for item in negative_list[985*fold_num+j*788:985*fold_num+(j+1)*788]:
            X.append(patients_info[item])
        y = np.concatenate((np.zeros(788) + 1, np.zeros(788)), axis=0)
        X = np.array(X)
        clf = RandomForestClassifier(max_depth=2, random_state=0)
        clf.fit(X, y)
        this_fold_test_result += clf.predict_proba(test)[:, 1]
        this_fold_validation_result += clf.predict_proba(validation_X)[:, 1]
    np.savetxt("./result/random_forest/fold_" + str(fold_num + 1) + "_test", this_fold_test_result)
    np.savetxt("./result/random_forest/fold_" + str(fold_num + 1) + "_validation", this_fold_validation_result)
