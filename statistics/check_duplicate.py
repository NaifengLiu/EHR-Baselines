events = []
with open("hae_result") as f:
    for line in f:
        events.append(line.replace("[", "").replace("\'", "").split(",")[0])
    f.close()
with open("nonhae_result") as f:
    for line in f:
        events.append(line.replace("[", "").replace("\'", "").split(",")[0])
    f.close()

print len(list(set(events)))

