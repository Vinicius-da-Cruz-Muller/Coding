import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Carregar o conjunto de dados
df = pd.read_csv("archive/Employee.csv")

# Pré-processar o conjunto de dados
df["Education"] = df["Education"].fillna("Unknown")
df["City"] = df["City"].fillna("Unknown")
df["Gender"] = df["Gender"].fillna("Unknown")

df = pd.get_dummies(df, columns=["Education", "City", "Gender","EverBenched"])

# Dividir o conjunto de dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(df.drop("LeaveOrNot", axis=1), df["LeaveOrNot"], test_size=0.6, random_state=0)

# Treinar uma árvore de decisão no conjunto de treinamento
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_train, y_train)

# Visualizar a árvore de decisão
plt.figure(figsize=(15,10))
plot_tree(clf, filled=True)
plt.show()

# Testar a acurácia da árvore de decisão no conjunto de teste
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Podar a árvore de decisão
path = clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas = path.ccp_alphas
ccp_alphas = ccp_alphas[:-1]

# Encontrar o melhor nível de poda
clfs = []
for ccp_alpha in ccp_alphas:
    clf = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha)
    clf.fit(X_train, y_train)
    clfs.append(clf)

# Avaliar o desempenho da árvore de decisão podada
accuracies = []
for clf in clfs:
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

# Selecionar o melhor modelo
best_clf = clfs[accuracies.index(max(accuracies))]

# Visualizar a árvore de decisão podada
plt.figure(figsize=(15,10))
plot_tree(clf, filled=True)
plt.show()

# Avaliar a acurácia da árvore de decisão podada no conjunto de teste
y_pred = best_clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy da árvore de decisão podada:", accuracy)
