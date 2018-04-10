from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
import numpy as np

X_train = np.loadtxt("./data/training/X")
y_train = np.loadtxt("./data/training/y")

X_test = np.loadtxt("./data/testing/X")
y_test = np.loadtxt("./data/testing/y")

X_unknown = np.loadtxt("./data/unknowndata/X")

clf = RandomForestClassifier(n_estimators=10, max_depth=5, oob_score=True)

clf.fit(X_train, y_train)

testing_labels = clf.predict(X_test)
testing_prob = clf.predict_proba(X_test)
np.savetxt("./data/testing/result_labels", testing_labels)
np.savetxt("./data/testing/result_prob", testing_prob)


print clf.oob_score_
print clf.score(X_test, y_test)


unknown_labels = clf.predict(X_unknown)
unknown_prob = clf.predict_proba(X_unknown)
np.savetxt("./data/unknowndata/result_labels", unknown_labels)
np.savetxt("./data/unknowndata/result_prob", unknown_prob)

