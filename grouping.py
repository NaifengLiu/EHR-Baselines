import random

matching = dict()

with open("./data/combined_matching") as f:
    for line in f:
        if int(float(line.split(",")[0])) not in matching:
            matching[int(float(line.split(",")[0]))] = []
        matching[int(float(line.split(",")[0]))].append(int(float(line.split(",")[1])))

random_matching = dict()

matching_keys = matching.keys()

negative_patients = []

for item in matching_keys:
    for everyone in matching[item]:
         negative_patients.append(everyone)

for i in range(len(matching_keys)):
    random_matching[matching_keys[i]] = negative_patients[i*200:(i+1)*200]
