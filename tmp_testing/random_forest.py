from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

X = np.loadtxt("result")
y = np.loadtxt("y")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = RandomForestClassifier(n_estimators=10, max_depth=5)

clf.fit(X_train, y_train)
labels = clf.predict(X_test)
prob = clf.predict_proba(X_test)

np.savetxt("labels", labels)
np.savetxt("prob", prob)
