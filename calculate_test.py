import grouping
import load_patient_info
import numpy as np
from tqdm import tqdm
from sklearn.ensemble import RandomForestClassifier
import pickle

matching = grouping.matching
matching_keys = matching.keys()
patients_info = load_patient_info.patients_info

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

this_fold_test_result = np.zeros(len(test))

print this_fold_test_result.shape

for i in range(1000):
    loaded_model = pickle.load(open('./model/' + str(i) + '.sav', 'rb'))
    tmp = loaded_model.predict_proba(test)[:, 1]
    print tmp.shape
    this_fold_test_result += tmp

np.savetxt("./result/bagging_random_forest/test", this_fold_test_result)
