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

#######################################################################################################################


X = []

for i in range(100):
    X.append(patients_info[x_train_file_names_positive[i]])
for i in range(100):
    X.append(patients_info[matching[x_train_file_names_positive[i]][0]])

X = np.array(X)

y = np.concatenate((np.zeros(100) + 1, np.zeros(100)), axis=0)

logistic = LogisticRegression()

logistic.fit(X, y)

print logistic.predict(X)
