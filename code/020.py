from numpy.core.fromnumeric import transpose
from numpy.lib.npyio import load
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split

iris=load_iris()
data=iris["data"]
target=iris["target"]

data_train,data_test,target_train,target_test = \
train_test_split(data,target,test_size=0.3)


