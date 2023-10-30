from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

train_data = pd.read_csv('knn.txt', delim_whitespace=True)
test_data = pd.read_csv('knn_teste.txt', delim_whitespace=True)

#print (train_data.columns)
X_train = train_data[['R','G','B']]
Y_train = train_data['Classes']
X_test = test_data[['R','G','B']]
y_test = test_data['Classes']

classes = train_data['Classes'].unique()

print("Conjunto de Treinamento:")
print(train_data.head())

print("Conjunto de Teste:")
print(test_data.head())

k_values  = [3, 5, 7]
predictions = {}

for k in k_values:
    print(f"K = {k}")
    
    predictions[k] = {}

    for classe in classes:
        knn = KNeighborsClassifier(n_neighbors=k)

        y_train_binary = (Y_train == classe)
        
        knn.fit(X_train, y_train_binary)
        
        y_pred = knn.predict(X_test)
        predictions[k][classe] = y_pred

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Acurácia para classe {classe}:{accuracy}")

# for k, k_predictions in predictions.items():
#     print(f"Acurácia para K = {k}: ")
#     for classe, y_pred in k_predictions.items():
#         accuracy = accuracy_score(y_test, y_pred)
#         print(f"Acurácia para classe {classe}: {accuracy}")



#não funcionaaaaaaaaaaaaaaaaaaaaaaaaaa