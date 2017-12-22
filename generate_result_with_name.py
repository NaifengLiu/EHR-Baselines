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

# r_result = np.zeros(248*201)
# for i in range(5):
#     r_result += np.loadtxt("result/bagging_random_forest/fold_"+str(i+1)+"_test").astype(float)
#
# l_result = np.zeros(248*201)
# for i in range(5):
#     l_result += np.loadtxt("result/bagging_logistic_regression/fold_"+str(i+1)+"_test").astype(float)

result = np.loadtxt("result/bagging_random_forest/test").astype(float)

print len(test)
print len(result)

with open("./result/combine_test_result", "w+") as w:
    for i in range(len(result)):
        w.write(str(test[i]))
        w.write(" ")
        if i < 248:
            w.write("1")
        else:
            w.write("0")
        w.write(" ")
        if float(result[i]) / float(1000) >= 0.5:
            w.write("1")
        else:
            w.write("0")
        w.write("\n")
