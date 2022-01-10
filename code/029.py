from sklearn.datasets import load_breast_cancer

breast_cancer = load_breast_cancer()

print(breast_cancer["DESCR"])

data=breast_cancer["data"]
target=breast_cancer["target"]

print(data.shape)
print(target.shape)

import numpy as np

all_data=np.c_[data,target]
print(all_data)
