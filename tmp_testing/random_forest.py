from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

X = np.loadtxt()
y = np.loadtxt()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

