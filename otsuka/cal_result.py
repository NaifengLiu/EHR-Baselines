import numpy as np

#           0              1       2       3             4          5
# ['BI_DIS_DEPRESSION', 'SCHIZ', 'MDD', 'OTH_PA', 'BI_DIS_MANIA', 'ANX']

y_result = np.loadtxt("./result/y_result")
y_truth = np.loadtxt("./data/y_test")

right = 0
wrong = 0

matrix = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

for i in range(len(y_truth)):
    matrix[int(y_truth[i])][int(y_result[i])] += 1

print matrix

tmp = []

order = [3, 5, 2, 4, 0, 1]

for row in matrix:
    row_tmp = []
    for i in order:
        row_tmp.append(row[i])
    tmp.append(row_tmp)

print "confusion matrix"

for i in order:
    print tmp[i]

result_prob = np.loadtxt("./result/y_result_prob")

prob = np.sum(result_prob, axis=0)

tmp = []

for i in order:
    tmp.append(prob[i])

print "chaid matrix"
print tmp






