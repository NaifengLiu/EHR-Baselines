test_data_len = 3
train_data_len = 5


def merge_data():
    with open("./data/test.csv", "w") as w:
        for i in range(0, test_data_len+1):
            with open("./data/test"+str(i)+".csv") as f:
                for line in f.readlines():
                    w.write(line)
                f.close()

    with open("./data/train.csv", "w") as w:
        for i in range(0, train_data_len+1):
            with open("./data/train"+str(i)+".csv") as f:
                for line in f.readlines():
                    w.write(line)
                f.close()


merge_data()
