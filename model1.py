from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pandas as pd
iris_dataset = load_iris()
import mglearn
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset["data"], iris_dataset["target"], random_state = 0
)

print format(iris_dataset.keys())


print iris_dataset["target_names"]


iris_dataFrame = pd.DataFrame(X_train, columns = iris_dataset.feature_names)

grr = pd.scatter_matrix(iris_dataFrame, c=y_train, figsize=(15,15),
    marker='o', s=60, alpha=.8, cmap=mglearn.cm3, hist_kwds={'bins':20})
# print iris_dataset["feature_names"]
# print iris_dataset["target"].size
# print "Shape of Data : {} ".format(iris_dataset["data"].shape)
# print iris_dataset["target"].size
