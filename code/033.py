from scipy.sparse.construct import random
from sklearn.datasets import load_breast_cancer

breast_cancer = load_breast_cancer()

print(breast_cancer["DESCR"])

data=breast_cancer["data"]
target=breast_cancer["target"]

print(data.shape)
print(target.shape)
import pandas as pd
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(
    data,target,random_state=40,test_size=0.25,stratify=target)

for name,array in zip(["target","y_train","y_test"],[target,y_train,y_test]) :
    print()
    print(name)
    print(pd.Series(array).value_counts(normalize=True))   
'''
target
target
1    0.627417
0    0.372583
dtype: float64

y_train
1    0.626761
0    0.373239
dtype: float64

y_test
1    0.629371
0    0.370629
dtype: float64
'''