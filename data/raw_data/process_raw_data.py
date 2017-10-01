from tqdm import tqdm
import csv

areas = ['WEST', 'SOUTH', 'NORTHEAST', 'MIDWEST', '']
genders = ['F', 'M', 'U', '']


def process_hae():
    with open("new.csv", "a") as w:
        with open('hae_pats.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if str(row[0])[0].isalpha():
                    continue
                if row[3] not in areas:
                    print row[3]
                    print row
                    areas.append(row[3])
                if row[1] not in genders:
                    print row[1]
                    print row
                    genders.append(row[1])

                for i in range(len(row)):
                    if i not in [1, 3, 4, 5]:
                        w.write(row[i])
                        w.write(",")
                    if i == 1:
                        w.write(str(genders.index(row[i])))
                        w.write(",")
                    if i == 3:
                        w.write(str(areas.index(row[i])))
                        w.write(",")
                w.write("\n")


def process_non_hae():
    with open("new2.csv", "a") as w:
        for j in range(1, 6):
            with open('nonhae_pats'+str(j)+'.csv') as f:
                reader = csv.reader(f)
                for row in reader:
                    if str(row[0])[0].isalpha():
                        continue
                    if row[4] not in areas:
                        print row[3]
                        print row
                        areas.append(row[3])
                    if row[2] not in genders:
                        print row[1]
                        print row
                        genders.append(row[1])

                    for i in range(len(row)):
                        if i-1 not in [-1, 1, 3, 4, 5]:
                            w.write(row[i].replace(",", ""))
                            w.write(",")
                        if i-1 == 1:
                            w.write(str(genders.index(row[i])))
                            w.write(",")
                        if i-1 == 3:
                            w.write(str(areas.index(row[i])))
                            w.write(",")
                    w.write("\n")
        w.close()


def combine():
    with open("../combined_data", "w") as w:
        with open("new.csv") as f1:
            with open("new2.csv") as f2:
                for lines in f1:
                    w.write(lines.rstrip()[:-3])
                    w.write("\n")
                for lines in f2:
                    w.write(lines.rstrip()[:-3])
                    w.write("\n")


process_hae()
process_non_hae()
combine()

