import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import ExtraTreeClassifier
import matplotlib.pyplot as plt
from sklearn import tree

import matplotlib.pyplot as plt

df = pd.read_csv("iris\iris.data", names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

X = df.drop("species", axis=1)
y = df["species"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

gnb = GaussianNB()
gnb.fit(X_train, y_train)

dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

etc = ExtraTreeClassifier()
etc.fit(X_train, y_train)

y_pred_gnb = gnb.predict(X_test)
y_pred_dtc = dtc.predict(X_test)
y_pred_etc = etc.predict(X_test)

accuracy_gnb = (y_pred_gnb == y_test).mean()
accuracy_dtc = (y_pred_dtc == y_test).mean()
accuracy_etc = (y_pred_etc == y_test).mean()

print("Precisão do modelo Bayesiano:", accuracy_gnb)
print("Precisão do modelo Decision Tree:", accuracy_dtc)
print("Precisão do modelo ExtraTree:", accuracy_etc)

plt.figure(figsize=(10, 10))
tree.plot_tree(dtc, feature_names=X.columns, class_names=y.unique(), filled=True, rounded=True)
plt.show()
