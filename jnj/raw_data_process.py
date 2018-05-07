import numpy as np
from sklearn import preprocessing

group = [[], [], [], [], [], [], [], []]

with open("./data/test.csv") as f:
    for lines in f.readlines():
        split = lines.rstrip().split(",")
        for i in range(8):
            if split[i] not in group[i]:
                group[i].append(split[i])
with open("./data/train.csv") as f:
    for lines in f.readlines():
        split = lines.rstrip().split(",")
        for i in range(8):
            if split[i] not in group[i]:
                group[i].append(split[i])

for sub_group in group:
    print sub_group

all_data = []

y_test = []
y_train = []
x_test_tmp = []
x_train_tmp = []

with open("./data/test.csv") as f:
    for lines in f.readlines():
        split = lines.rstrip().split(",")
        tmp_x = []
        y_test.append(group[7].index(split[7]))
        for i in range(7):
            tmp_x.append(group[i].index(split[i]))
        all_data.append(tmp_x)
        x_test_tmp.append(tmp_x)
    f.close()

y_test = np.array(y_test)
print y_test.shape
np.savetxt("./data/y_test", y_test)

with open("./data/train.csv") as f:
    for lines in f.readlines():
        split = lines.rstrip().split(",")
        tmp_x = []
        y_train.append(group[7].index(split[7]))
        for i in range(7):
            tmp_x.append(group[i].index(split[i]))
        all_data.append(tmp_x)
        x_train_tmp.append(tmp_x)
    f.close()

y_train = np.array(y_train)
print y_train.shape
np.savetxt("./data/y_train", y_train)

enc = preprocessing.OneHotEncoder()
enc.fit(all_data)

x_test = enc.transform(x_test_tmp).toarray()
x_train = enc.transform(x_train_tmp).toarray()

x_test = np.array(x_test)
x_train = np.array(x_train)

print x_test.shape
print x_train.shape
np.savetxt("./data/x_test", x_test)
np.savetxt("./data/x_train", x_train)

