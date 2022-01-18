import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

train=pd.read_csv("039.csv")
test=pd.read_csv("040.csv")

# print(df)

scalar=StandardScaler()
scalar.fit(train)

df_train=scalar.transform(train)
df_test=scalar.transform(test)


print(scalar.var_,scalar.mean_)

