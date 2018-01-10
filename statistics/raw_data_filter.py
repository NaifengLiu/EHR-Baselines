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

with open("data/hae_all_1.csv") as f:
    with open("data/new_hae.csv", "w+") as w:
        for line in f:
            if line.split(",")[1] in events:
                w.write(line)

with open("data/nonhae.csv") as f:
    with open("data/new_non_hae.csv", "w+") as w:
        for line in f:
            if line.split(",")[1] in events:
                w.write(line)
