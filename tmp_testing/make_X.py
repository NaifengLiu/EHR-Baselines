# 1 3 5 6 7 8
import numpy as np
from sklearn import preprocessing

tmp = []

tmp_tmp = []

with open("./data/training/X.csv", "w+") as w:
    with open("./data/training/training.csv") as f:
        lines = f.readlines()

        q = 0

        for line in lines:
            split = line.rstrip().split(",")
            line_tmp = []
            for i in [1, 3, 5, 6, 7, 8]:
                if split[i] != "":
                    line_tmp.append(split[i])
                else:
                    line_tmp.append("10101010")
            if len(line_tmp) == 6:
                tmp.append(line_tmp)

            tmp_tmp.append([split[2], split[4], split[9], split[10]])

            q += 1

            if q >= 10:
                break

        enc = preprocessing.OneHotEncoder()
        enc.fit(tmp_tmp)

        pmt = enc.transform(tmp_tmp).toarray()
        print pmt

        result = []

        for i in range(len(tmp)):
            result.append(tmp[i] + pmt[i].astype(int).tolist())

        print result

        # result = np.array(result).astype(int)
        # np.savetxt("result", result)


