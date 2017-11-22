with open("./raw_data/hae_pats.csv") as f:
    title = f.readline().split(",")
    print len(title)

title.pop(0)
del title[-1]
title.remove("IDX_DT")
title.remove("LOOKBACK_DT")

print len(title)

title_index = []

for i in range(len(title)):
    if len(title[i].split("ER_")) != 2:
        if len(title[i].split("PRC_")) != 2:
            if len(title[i].split("lookback_")) != 2:
                title_index.append(i)
                # print title[i]

print title_index
print len(title_index)


