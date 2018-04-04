from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
import numpy as np

X = np.loadtxt("result")
y = np.loadtxt("y")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

X_train = np.delete(X_train, 0, axis=1)
x_test_id = X_test[:, 0]
X_test = np.delete(X_test, 0, axis=1)

clf = RandomForestClassifier(n_estimators=10, max_depth=5, oob_score=True)

clf.fit(X_train, y_train)
labels = clf.predict(X_test)
prob = clf.predict_proba(X_test)

np.savetxt("labels", labels)
np.savetxt("ytest", y_test)
np.savetxt("prob", prob)

max_p = np.amax(prob, axis=1)

tmp = np.stack((x_test_id, labels, max_p)).T

print tmp.shape

np.savetxt("output", tmp)

print clf.oob_score_

print clf.score(X_test, y_test)
