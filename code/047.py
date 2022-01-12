import numpy as np
import pandas as pd
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

np.random.seed(42)
raw_data = make_moons(n_samples=2000, noise=0.25,random_state=42)
data=raw_data[0]
target=raw_data[1]

print(data.shape,target.shape)

x_train,x_test,y_train,y_test=train_test_split(data,target)

classifer=DecisionTreeClassifier()
classifer.fit(x_train,y_train)
# DecisionTreeClassifier()
print(classifer.score(x_test,y_test))