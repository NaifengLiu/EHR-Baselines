import numpy as np
import scipy
import collections

hae_patient = dict()
non_hae_patient = dict()


def fill_with_data(patient, file_address):
    with open(file_address) as f:
        for line in f:
            line_split = line.rstrip().split(",")
            if line_split[0] not in patient:
                patient[line_split[0]] = []
            else:
                patient[line_split[0]].append(line_split[1])
    return patient


fill_with_data(hae_patient, "data/hae_all_1.csv")
fill_with_data(non_hae_patient, "data/nonhae_all_1.csv")


def get_top_m_events_from_n_patients(patient, m, n):
    for person in patient.keys()[0:n]:
        print person
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
        print result
        print ""


print "hae patients:"
get_top_m_events_from_n_patients(hae_patient, 10, 100)
print "non hae patients:"
get_top_m_events_from_n_patients(non_hae_patient, 10, 100)