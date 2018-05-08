# classes = ['ISCHEMIC_STROKE', 'CAD_ONLY', 'CAD_ACS', 'ACS', 'AFIB', 'PAD_ONLY', 'ALL_OTHER', 'CHF']
classes = ['PAD_ACS']

for this_class in classes:
    with open("./data/subdata/"+this_class, "w+") as w:
        num = 0
        with open("./data/train.csv") as f:
            for line in f.readlines():
                class_name = line.rstrip().split(",")[-1]
                if class_name == this_class:
                    if num < 3400:
                        w.write(line)
                        num += 1
            f.close()
        w.close()

