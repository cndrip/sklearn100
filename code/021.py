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
# 逻辑回归 模型
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000) #训练1000次
model.fit(data_train,target_train)

s1=model.score(data_train,target_train)
print(s1)
s2=model.score(data_test,target_test)
print(s2)