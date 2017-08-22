from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
iris_dataset = load_iris()

print("keys of iris \n {}".format(iris_dataset.keys()))

X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state = 0)


# K Nearest Neighbours
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

X_new = np.array([[1,1,1,1]])
prediction = knn.predict(X_new)
print iris_dataset["target_names"][prediction]


#Calculating the score of the Algorithm
print "The overall score of KNN is {}\n".format(knn.score(X_test, y_test))