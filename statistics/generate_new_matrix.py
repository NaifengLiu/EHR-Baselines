import numpy as np
from tqdm import tqdm
from datetime import datetime

all_hae_records = []
hae_file_address = "data/hae_all_1.csv"
all_non_hae_records = []
non_hae_file_address = "data/nonhae.csv"

all_days = np.arange('2010-01-01', '2015-08-01', dtype='datetime64[D]')
days = []
for day in all_days:
    days.append(str(day).replace("-", ""))

events = []
with open("hae_result") as ff:
    for line in ff:
        events.append(line.replace("[", "").replace("\'", "").split(",")[0])
    ff.close()
with open("nonhae_result") as ff:
    for line in ff:
        events.append(line.replace("[", "").replace("\'", "").split(",")[0])
    ff.close()

events = list(set(events))
print events


def add_to_records(address, records):
    with open(address) as f:
        for the_line in f:
            line_split = the_line.rstrip().split(",")
            if line_split[1] in events:
                records.append([line_split[0], line_split[1], line_split[2]])
        f.close()
    records.sort(key=lambda x: x[1], reverse=True)


add_to_records(hae_file_address, all_hae_records)

previous_person_matrix = np.zeros((4019, 2038))
previous_person_id = ""
a = 0

for i in tqdm(range(len(all_hae_records))):
    each_record = all_hae_records[i]
    if each_record[0] != previous_person_id:
        if previous_person_id != "":
            a += 1
            # np.savetxt("output/hae/" + previous_person_id, previous_person_matrix)
            # print previous_person_id + ", " + str(np.sum(previous_person_matrix))
            # print previous_person_matrix.shape
        previous_person_matrix = np.zeros((4019, 2038))
        previous_person_id = each_record[0]
    previous_person_matrix[events.index(each_record[1]), days.index(each_record[2])] += 1

    if i == len(all_hae_records) - 1:
        np.savetxt("output/hae/" + previous_person_id, previous_person_matrix)
        print previous_person_id + ", " + str(np.sum(previous_person_matrix))
