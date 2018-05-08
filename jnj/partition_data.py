# classes_40800 = ['ISCHEMIC_STROKE', 'CAD_ONLY', 'CAD_ACS', 'ACS', 'AFIB', 'PAD_ONLY', 'ALL_OTHER', 'CHF']
# classes_3400 = ['PAD_ACS']

# 40800, 3400

# for this_class in classes:
#     with open("./data/subdata/"+this_class, "w+") as w:
#         num = 0
#         with open("./data/train.csv") as f:
#             for line in f.readlines():
#                 class_name = line.rstrip().split(",")[-1]
#                 if class_name == this_class:
#                     if num < 3400:
#                         w.write(line)
#                         num += 1
#             f.close()
#         w.close()

# for i in range(12):
#     with open("data/5_fold_data/undersampling_data/" + str(i), "w") as w:
#         for this_class in classes_40800:
#             with open("./data/subdata/" + this_class) as f:
#                 lines = f.readlines()
#                 for line in lines[i * 3400:(i + 1) * 3400]:
#                     w.write(line)
#                 f.close()
#         for this_class in classes_3400:
#             with open("./data/subdata/" + this_class) as f:
#                 lines = f.readlines()
#                 for line in lines:
#                     w.write(line)
#                 f.close()
#         w.close()

# for i in range(12):
#     with open("data/5_fold_data/undersampling_data/" + str(i)) as f:
#         print len(f.readlines())

a = range(3400)
folds_index = []
for i in range(5):
    b = range(i*680, (i+1)*680)
    c = [item for item in a if item not in b]
    folds_index.append(c)

print folds_index

for i in range(5):
    for j in range(12):
        with open("./data/5_fold_data/" + str(i) + "_" + str(j), "w") as w:
            with open("./data/5_fold_data/undersampling_data/" + str(j)) as f:
                lines = f.readlines()
                for k in range(9):
                    this_class = lines[k*3400:(k+1)*3400]
                    tmp = this_class[folds_index[i]]
                    for line in tmp:
                        w.write(line)
                f.close()
            w.close()


