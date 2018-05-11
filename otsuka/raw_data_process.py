
n_index = [3, 4, 5, 6]
s_index = [0, 7, 8, 9, 10, 11, 12]


def merge_files():
    with open("./data/test", "w") as w:
        for i in range(2):
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
        for i in range(3):
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









