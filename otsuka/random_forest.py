from sklearn.ensemble import RandomForestClassifier
import numpy as np

print "loading data ..."

X_train = np.loadtxt("./data/x_train")
y_train = np.loadtxt("./data/y_train")

X_test = np.loadtxt("./data/x_test")
y_test = np.loadtxt("./data/y_test")

clf = RandomForestClassifier(n_estimators=50, max_depth=10)

print "fitting ..."

clf.fit(X_train, y_train)

print "predicting ..."

y_result = clf.predict(X_test)
y_result_prob = clf.predict_proba(X_test)

print "saving result ..."

np.savetxt("./result/y_result", y_result)
np.savetxt("./result/y_result_prob", y_result_prob)
