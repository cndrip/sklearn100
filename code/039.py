import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

df=pd.read_csv(r"E:\bigdata\sklearn100\code\039.csv")
# print(df)

scalar=StandardScaler()
scalar.fit(df)
df_scaled=scalar.transform(df)

print(df_scaled)

