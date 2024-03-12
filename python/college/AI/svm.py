import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carregar base de dados
df = pd.read_csv("archive/Employee.csv")

# Pré-processar o conjunto de dados
df["Education"] = df["Education"].fillna("Unknown")
df["City"] = df["City"].fillna("Unknown")
df["Gender"] = df["Gender"].fillna("Unknown")

df = pd.get_dummies(df, columns=["Education", "City", "Gender","EverBenched"])

# Selecionar características e variável alvo
X = df.drop("LeaveOrNot", axis=1)
y = df["LeaveOrNot"]

# Dividir dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Criar lista de kernels
kernels = ["linear", "poly", "rbf", "sigmoid"]

# Armazenar resultados
resultados = {}

# Treinar SVM com cada kernel e avaliar a acurácia
for kernel in kernels:
    clf = SVC(kernel=kernel)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    resultados[kernel] = accuracy

# Mostrar resultados
for kernel, accuracy in resultados.items():
    print(f"Kernel: {kernel} - Acurácia: {accuracy}")
