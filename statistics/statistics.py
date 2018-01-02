import numpy as np
import scipy
import collections
from tqdm import tqdm

hae_patient = dict()
non_hae_patient = dict()
events = []


def check_total_events():
    with open("data/hae_all_1.csv") as f:
        for line in f:
            line_split = line.rstrip().split(",")
            if line_split[1] not in events:
                events.append(line_split[1])
        f.close()
    with open("data/nonhae.csv") as f:
        print type(f.readlines())
        for i in tqdm(range(len(f.readlines()))):
            line = f.readlines()[i]
            line_split = line.rstrip().split(",")
            if line_split[1] not in events:
                events.append(line_split[1])
        f.close()
    print len(events)


check_total_events()


def fill_with_data(patient, file_address):
    with open(file_address) as f:
        for line in f:
            line_split = line.rstrip().split(",")
            if line_split[0] not in patient:
                patient[line_split[0]] = []
            else:
                patient[line_split[0]].append(line_split[1])
    return patient


# fill_with_data(hae_patient, "data/hae_all_1.csv")
# fill_with_data(non_hae_patient, "data/nonhae_all_1.csv")


def get_top_m_events_from_n_patients(patient, m, n):
    all_results = []
    for person in patient.keys()[0:n]:
        # print person
        counter = collections.Counter(patient[person])
        print counter
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


print "hae patients:"
# hae_result = get_top_m_events_from_n_patients(hae_patient, 10, 100)
print "non hae patients:"
# non_hae_result = get_top_m_events_from_n_patients(non_hae_patient, 10, 100)
#
# all_days = np.arange('2010-01-01', '2015-08-01', dtype='datetime64[D]')
# days_tmp = []
# for d in all_days:
#     days_tmp.append(str(d).replace("-", ""))


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
