from sklearn.ensemble import RandomForestClassifier
import numpy as np

X_train = np.loadtxt("./data/x_train")
y_train = np.loadtxt("./data/y_train")

X_test = np.loadtxt("./data/x_test")
y_test = np.loadtxt("./data/y_test")

clf = RandomForestClassifier(n_estimators=50, max_depth=10, oob_score=True)

clf.fit(X_train, y_train)

y_result = clf.predict(X_test)
y_result_prob = clf.predict_proba(X_test)
np.savetxt("./result/y_result", y_result)
np.savetxt("./result/y_result_prob", y_result_prob)
