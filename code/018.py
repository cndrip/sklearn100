from numpy.lib.npyio import load
from sklearn.datasets import load_iris
import pandas as pd

iris=load_iris()

vdata=pd.DataFrame(data=iris["data"],columns=iris["feature_names"])
# print(type(iris))
# print(iris.keys())
# print(iris["filename"])
# print(iris["data"][:5])
print(vdata)