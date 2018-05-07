import numpy as np

y_result = np.loadtxt("./result/y_result")
y_truth = np.loadtxt("./data/y_test")

right = 0
wrong = 0

for i in range(len(y_result)):
    if y_result[i] == y_truth[i]:
        right += 1
    else:
        wrong += 1

print right
print wrong



