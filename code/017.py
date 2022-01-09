from numpy.lib.npyio import load
from sklearn.datasets import load_iris

iris=load_iris()
print(type(iris))
print(iris.keys())
print(iris["filename"])
print(iris["data"][:5])