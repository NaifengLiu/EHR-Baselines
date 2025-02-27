import numpy as np
import scipy
import collections
from tqdm import tqdm
from sklearn.neighbors import KNeighborsClassifier

hae_patient = dict()
non_hae_patient = dict()
hae_patient_data = dict()
non_hae_patient_data = dict()

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


def fill_with_data(patient, file_address):
    with open(file_address) as f:
        lines = f.readlines()
        for i in tqdm(range(len(lines))):
            line = lines[i]
            line_split = line.rstrip().split(",")
            if line_split[0] not in patient:
                patient[line_split[0]] = []
            else:
                patient[line_split[0]].append(line_split[1])
    return patient


fill_with_data(hae_patient, "data/hae_all_1.csv")
fill_with_data(non_hae_patient, "data/nonhae.csv")


def get_top_m_events_from_n_patients(patient, m, n):
    all_results = []
    for person in patient.keys()[0:n]:
        # print person
        counter = collections.Counter(patient[person])
        print counter
        print counter.keys()
        print counter.values()
        tmp = []
        for i in range(len(counter.values())):
            tmp.append([i, np.var(
                np.concatenate((np.zeros(counter.values()[i]) + 1, np.zeros(2038 - counter.values()[i])), axis=0))])
        tmp.sort(key=lambda x: x[1], reverse=True)
        result = []
        for item in tmp[0:m]:
            result.append(counter.keys()[item[0]])
        # print result
        all_results.append([person, result])
    return all_results


def get_top_m_events(patient, m):
    result = []
    event_dict = dict()
    for i in tqdm(range(len(patient.keys()))):
        # print
        person = patient.keys()[i]
        counter = collections.Counter(patient[person])
        for j in range(len(counter.keys())):
            if counter.keys()[j] not in event_dict:
                event_dict[counter.keys()[j]] = []
            event_dict[counter.keys()[j]].append(counter.values()[j])
    for event in event_dict.keys():
        tmp = np.pad(event_dict[event], (0, len(patient.keys()) - len(event_dict[event])), 'constant')
        result.append([event, np.var(tmp)])
    result.sort(key=lambda x: x[1], reverse=True)
    for item in result[0:m]:
        print item


# get_top_m_events(hae_patient, 2901)

# get_top_m_events(non_hae_patient, 2901)


# hae_result = get_top_m_events_from_n_patients(hae_patient, 10, 100)
# non_hae_result = get_top_m_events_from_n_patients(non_hae_patient, 10, 100)
#
all_days = np.arange('2010-01-01', '2015-08-01', dtype='datetime64[D]')
days_tmp = []
for d in all_days:
    days_tmp.append(str(d).replace("-", ""))


def generate_matrix(patient_type, original_file_path, previous_result):
    for each_person in previous_result:
        his_name = each_person[0]
        his_events = each_person[1]
        his_matrix = []
        for each_event in his_events:
            day_dict = dict()
            for day in all_days:
                day_dict[str(day).replace("-", "")] = 0
            with open(original_file_path) as f:
                for line in f:
                    line_split = line.rstrip().split(",")
                    if line_split[0] == his_name and line_split[1] == each_event:
                        day_dict[line_split[2]] += 1
            tmp_result = []
            for day in days_tmp:
                tmp_result.append(day_dict[day])
            his_matrix.append(tmp_result)
        his_matrix = np.array(his_matrix)
        print his_matrix
        print his_matrix.shape
        print np.sum(his_matrix)
        np.savetxt("output/" + patient_type + "/" + his_name, his_matrix)


# generate_matrix("non_hae", "data/nonhae_all_1.csv", non_hae_result)
# generate_matrix("hae", "data/hae_all_1.csv", hae_result)

def get_patient_array(patient, patient_data, tag, n):
    for person in patient.keys()[0:n]:
        # print person
        counter = collections.Counter(patient[person])
        # print counter
        # print counter.keys()
        # print counter.values()
        tmp = []
        for event in events:
            if event in counter.keys():
                tmp.append(counter.values()[counter.keys().index(event)])
            else:
                tmp.append(0)
        # print len(tmp)
        # print person
        # print tmp
        # patient_data[person] = tmp
        tmp = np.array(tmp)
        if tag == 1:
            np.savetxt("data/person/hae/" + person, tmp)
        elif tag == 0:
            np.savetxt("data/person/nonhae/" + person, tmp)


get_patient_array(hae_patient, hae_patient_data, 1)
get_patient_array(non_hae_patient, non_hae_patient_data, 0)

# X = []
#
# for item in hae_patient_data.keys()[0:986]:
#     X.append(hae_patient_data[item])
# for item in non_hae_patient_data.keys()[0:986*200]:
#     X.append(non_hae_patient_data[item])
#
# y = np.concatenate(
#     (np.zeros(int(len(hae_patient_data.keys()) * 0.8)) + 1, np.zeros(int(len(non_hae_patient_data.keys()) * 0.8))),
#     axis=0)
#
# neigh = KNeighborsClassifier(n_neighbors=3)
# neigh.fit(X, y)
#
# test_X = []
# for item in hae_patient_data.keys()[986:1233]:
#     test_X.append(hae_patient_data[item])
# for item in non_hae_patient_data.keys()[986*200:1233*200]:
#     test_X.append(non_hae_patient_data[item])
#
# test_y = neigh.predict(test_X)
#
# print test_y
