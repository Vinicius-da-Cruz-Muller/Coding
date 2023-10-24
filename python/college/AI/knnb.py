from sklearn.neighbors import KNeighborsClassifier

r = [1, 2, 6, 7, 10, 3, 100, 250, 243, 210, 200, 215, 56, 79, 80, 95, 80, 49]
g = [10, 20, 25, 45, 50, 24, 4, 7, 5, 2, 1, 0, 200, 234, 210, 200, 210, 207]
b = [200, 230, 150, 100, 125, 111, 10, 50, 68, 90, 95, 68, 1, 3, 8, 10, 4, 1]
classes = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]

data = list(zip(r, g, b))
points = [(1, 2, 100), (10, 20, 30), (8, 5, 20), (237, 45, 100), (1, 50, 101), (67, 121, 12)]

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(data, classes)
print("K = 3")
for point in points:
    prediction = knn.predict([point])
    print(f"R: {point[0]}, G: {point[1]}, B: {point[2]} - Classe: {prediction}")

print("-------------------------------\n"
      "K = 5")
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(data, classes)
for point in points:
    prediction = knn.predict([point])
    print(f"R: {point[0]}, G: {point[1]}, B: {point[2]} - Classe: {prediction}")

print("-------------------------------\n"
      "K = 7")
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(data, classes)
for point in points:
    prediction = knn.predict([point])
    print(f"R: {point[0]}, G: {point[1]}, B: {point[2]} - Classe: {prediction}")
print("-------------------------------")