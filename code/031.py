from sklearn.datasets import load_breast_cancer

breast_cancer = load_breast_cancer()

print(breast_cancer["DESCR"])

data=breast_cancer["data"]
target=breast_cancer["target"]

print(data.shape)
print(target.shape)

import numpy as np
import pandas as pd

df =pd.DataFrame(
    np.c_[data,target],
    columns=list(breast_cancer["feature_names"])+["target"]
)
print(df.head(3))
