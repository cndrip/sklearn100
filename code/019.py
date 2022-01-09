from numpy.lib.npyio import load
from sklearn.datasets import load_iris
import pandas as pd

iris=load_iris()
data=iris["data"]
print(type(data.shape)) # (150,4)
target=iris["target"]

print(pd.Series(target).unique()) # [0,1,2]

# vdata=pd.DataFrame(data=iris["data"],columns=iris["feature_names"])
# print(iris["target_names"])
# print(type(iris))
# print(iris.keys())
# print(iris["filename"])
# print(iris["data"][:5])
# print(vdata)