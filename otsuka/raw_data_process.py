import numpy as np
from sklearn import preprocessing

n_index = [3, 4, 5, 6]
s_index = [0, 7, 8, 9, 11, 12]


def merge_files():
    with open("./data/test", "w") as w:
        for i in range(1, 3):
            with open("./data/test" + str(i) + ".csv") as f:
                f.readline()
                for line in f.readlines():
                    split = line.rstrip().split(",")
                    for j in n_index:
                        if split[j] == "":
                            w.write("10101010")
                        else:
                            w.write(split[j])
                        w.write(",")
                    for j in s_index:
                        w.write(split[j])
                        if j != 12:
                            w.write(",")
                        else:
                            w.write("\n")

    with open("./data/train", "w") as w:
        for i in range(1, 4):
            with open("./data/train" + str(i) + ".csv") as f:
                f.readline()
                for line in f.readlines():
                    split = line.rstrip().split(",")
                    for j in n_index:
                        if split[j] == "":
                            w.write("10101010")
                        else:
                            w.write(split[j])
                        w.write(",")
                    for j in s_index:
                        w.write(split[j])
                        if j != 12:
                            w.write(",")
                        else:
                            w.write("\n")


# merge_files()


def process_data():
    group = [[], [], [], [], [], [], [], [], [], []]

    with open("./data/test") as f:
        for lines in f.readlines():
            split = lines.rstrip().split(",")
            for i in range(4, 10):
                if split[i] not in group[i]:
                    group[i].append(split[i])
    with open("./data/train") as f:
        for lines in f.readlines():
            split = lines.rstrip().split(",")
            for i in range(4, 10):
                if split[i] not in group[i]:
                    group[i].append(split[i])

    for sub_group in group:
        print sub_group

    all_data = []
    y_test = []
    y_train = []
    x_test_tmp_0 = []
    x_test_tmp_1 = []
    x_train_tmp_0 = []
    x_train_tmp_1 = []
    x_test_final = []
    x_train_final = []

    with open("./data/test") as f:
        for lines in f.readlines():
            split = lines.rstrip().split(",")
            tmp_x_0 = []
            tmp_x_1 = []
            y_test.append(group[9].index(split[9]))
            for i in range(4):
                tmp_x_0.append(split[i])
            tmp_x_0 = map(float, tmp_x_0)
            x_test_tmp_0.append(tmp_x_0)
            for i in range(4, 9):
                tmp_x_1.append(group[i].index(split[i]))
            all_data.append(tmp_x_1)
            x_test_tmp_1.append(tmp_x_1)
        f.close()

    y_test = np.array(y_test)
    print y_test.shape
    np.savetxt("./data/y_test", y_test)

    with open("./data/train") as f:
        for lines in f.readlines():
            split = lines.rstrip().split(",")
            tmp_x_0 = []
            tmp_x_1 = []
            y_train.append(group[9].index(split[9]))
            for i in range(4):
                tmp_x_0.append(split[i])
            tmp_x_0 = map(float, tmp_x_0)
            x_train_tmp_0.append(tmp_x_0)
            for i in range(4, 9):
                tmp_x_1.append(group[i].index(split[i]))
            all_data.append(tmp_x_1)
            x_train_tmp_1.append(tmp_x_1)
        f.close()

    y_train = np.array(y_train)
    print y_train.shape
    np.savetxt("./data/y_train", y_train)

    enc = preprocessing.OneHotEncoder()
    enc.fit(all_data)

    x_test = enc.transform(x_test_tmp_1).toarray()
    x_train = enc.transform(x_train_tmp_1).toarray()

    for i in range(len(x_test_tmp_0)):
        x_test_final.append(x_test_tmp_0[i] + x_test[i].astype(int).tolist())
    result = np.array(x_test_final)
    print result.shape
    np.savetxt("./data/x_test", result)

    for i in range(len(x_train_tmp_0)):
        x_train_final.append(x_train_tmp_0[i] + x_train[i].astype(int).tolist())
    result = np.array(x_train_final)
    print result.shape
    np.savetxt("./data/x_test", result)


process_data()












