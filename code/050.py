import numpy as np
import pandas as pd
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

np.random.seed(42)
raw_data = make_moons(n_samples=2000, noise=0.25,random_state=42)
data=raw_data[0]
target=raw_data[1]

x_train,x_test,y_train,y_test=train_test_split(data,target)

from sklearn.model_selection import GridSearchCV

param={
    "max_depth":np.arange(1,10),
    "min_samples_leaf":np.arange(1,10)
}
classifer=DecisionTreeClassifier()

grid_search=GridSearchCV(    
        classifer,
        param_grid=param,
        scoring="accuracy",
        cv=5
)
grid_search.fit(x_train,y_train)
print(grid_search.best_estimator_)
# print(classifer.score(x_test,y_test))