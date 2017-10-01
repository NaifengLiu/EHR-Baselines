import grouping
import load_patient_info
import numpy as np
from sklearn.linear_model import LogisticRegression

matching = grouping.matching
missing = [1, 3, 8, 72, 165, 183, 223, 239, 285, 305, 324, 348, 376, 416, 446, 461, 486, 489, 548, 575, 599, 612, 632,
           682, 683, 718, 721, 757, 777, 792, 799, 816, 819, 998, 1023, 1034, 1075, 1080, 1118, 1123, 1132, 1146, 1166,
           1215]
matching_keys = matching.keys()
patients_info = load_patient_info.patients_info
#######################################################################################################################
x_train_file_names_positive = []
x_test_file_names_positive = []

for i in range(len(matching_keys)):
    if i not in missing:
        if len(x_train_file_names_positive) < 985:
            x_train_file_names_positive.append(matching_keys[i])
        else:
            x_test_file_names_positive.append((matching_keys[i]))

x_train_file_names_negative = []
for i in range(200):
    for item in x_train_file_names_positive:
        x_train_file_names_negative.append(matching[item][i])
x_test_file_names_negative = []
for i in range(200):
    for item in x_test_file_names_positive:
        x_test_file_names_negative.append(matching[item][i])

test = []
for patient in x_test_file_names_positive:
    test.append(patients_info[patient])
for patient in x_test_file_names_positive:
    for non_patient in matching[patient]:
        test.append(patients_info[non_patient])
test = np.array(test)

#######################################################################################################################

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
    this_fold_validation_result = np.zeros(197)

    for j in range(5):
        X = []
        for item in tmp_training_names_positive:
            X.append(patients_info[item])
        for item in tmp_training_names_positive:
            X.append(matching[item][j])
        y = np.concatenate((np.zeros(788) + 1, np.zeros(788)), axis=0)
        X = np.array(X)
        logistic = LogisticRegression()
        logistic.fit(X, y)
        this_fold_validation_result += logistic.predict(validation_X)
        print len(this_fold_validation_result)
        print this_fold_validation_result.shape
        print this_fold_validation_result