import grouping
import load_patient_info
import numpy as np
from tqdm import tqdm
from sklearn.ensemble import RandomForestClassifier
import random
import os

matching = grouping.random_matching
matching_keys = matching.keys()
patients_info = load_patient_info.patients_info


def main(n):
    if not os.path.exists("./result/random_forest_"+str(n)):
        os.makedirs("./result/random_forest_"+str(n))
    x_train_file_names_positive = []
    x_test_file_names_positive = []

    for i in range(len(matching_keys)):
        if len(x_train_file_names_positive) < n:
            x_train_file_names_positive.append(matching_keys[i])
        else:
            x_test_file_names_positive.append((matching_keys[i]))

    random.shuffle(x_train_file_names_positive)

    test = []
    for patient in x_test_file_names_positive:
        test.append(patients_info[patient])
    for patient in x_test_file_names_positive:
        for non_patient in matching[patient]:
            test.append(patients_info[non_patient])
    test = np.array(test)

    for fold_num in range(5):
        print("start " + str(fold_num + 1) + " fold")
        tmp_validation_names_positive = x_train_file_names_positive[fold_num * n/5:(fold_num + 1) * n/5]
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
            y = np.concatenate((np.zeros(n/5*4) + 1, np.zeros(n/5*4)), axis=0)
            X = np.array(X)
            clf = RandomForestClassifier(max_depth=2, random_state=0)
            clf.fit(X, y)
            this_fold_test_result += clf.predict_proba(test)[:, 1]
            this_fold_validation_result += clf.predict_proba(validation_X)[:, 1]
        np.savetxt("./result/random_forest_"+str(n)+"/fold_" + str(fold_num+1) + "_test", this_fold_test_result)
        np.savetxt("./result/random_forest_"+str(n)+"/fold_" + str(fold_num+1) + "_validation", this_fold_validation_result)


for i in [985, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 50]:
    main(i)
