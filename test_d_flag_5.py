import grouping
import load_patient_info

matching = grouping.matching
matching_keys = matching.keys()
patients_info = load_patient_info.patients_info

i = 0
m = 0
for each in matching_keys:
    m += patients_info[each][0]
    i += 1

j = 0
n = 0
for each in matching_keys:
    for everyone in matching[each]:
        n += patients_info[everyone][0]
        j += 1

print i
print j
print m
print n

print float(m)/float(i)
print float(n)/float(j)
