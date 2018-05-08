from sklearn.ensemble import RandomForestClassifier
import numpy as np

X_test = np.loadtxt("./data/x_test")
y_test = np.loadtxt("./data/y_test")

for i in range(5):
    for j in range(12):
        X_train = np.loadtxt("./data/5_fold_data/" + str(i) + "_" + str(j) + "_x")
        y_train = np.loadtxt("./data/5_fold_data/" + str(i) + "_" + str(j) + "_y")
        clf = RandomForestClassifier(n_estimators=50, max_depth=10)
        clf.fit(X_train, y_train)
        y_result_prob = clf.predict_proba(X_test)
        np.savetxt("./result/5_fold_result/" + str(i) + "_" + str(j), y_result_prob)
