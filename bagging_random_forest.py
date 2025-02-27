import grouping
import load_patient_info
import numpy as np
from tqdm import tqdm
from sklearn.ensemble import RandomForestClassifier
import pickle

# Step 1: matching part
#
# for each HAE patient, we identify a list of 200 non-HAE patients

matching = grouping.matching
matching_keys = matching.keys()
patients_info = load_patient_info.patients_info

count = 0

#######################################################################################################################

# Step 2:
# Separate the 1233 HAEs to a 80% training HAE set (985), denoted as TrP, and a 20% testing HAE set (247),
# denoted as TeP.

x_train_file_names_positive = []
x_test_file_names_positive = []

for i in range(len(matching_keys)):
    # For the training HAE set, we identify their matched non - HAE et(986 * 200 = 197, 200), denoted as TrN.
    if len(x_train_file_names_positive) < 985:
        x_train_file_names_positive.append(matching_keys[i])
    # For the testing HAE set, we identify their matched non-HAE set (247 * 200 = 49,400), denoted as TeN.
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

# Step 3: Training process based on TrP + TrN.
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
    this_fold_validation_result = np.zeros(len(validation_X))
    for j in tqdm(range(200)):
        X = []
        for item in tmp_training_names_positive:
            X.append(patients_info[item])
        for item in tmp_training_names_positive:
            X.append(patients_info[matching[item][j]])
        y = np.concatenate((np.zeros(788) + 1, np.zeros(788)), axis=0)
        X = np.array(X)
        clf = RandomForestClassifier(max_depth=2)
        clf.fit(X, y)
        # this_fold_test_result += clf.predict_proba(test)[:, 1]
        # this_fold_validation_result += clf.predict_proba(validation_X)[:, 1]

        # Out:  5 folder cross validation results.
        this_fold_validation_result += clf.predict(validation_X)
        filename = './model/' + str(count) + '.sav'
        # Out: training model
        pickle.dump(clf, open(filename, 'wb'))
        count += 1
    # np.savetxt("./result/bagging_random_forest/fold_" + str(fold_num+1) + "_test", this_fold_test_result)
    np.savetxt("./result/bagging_random_forest/fold_" + str(fold_num+1) + "_validation_predict", this_fold_validation_result)
