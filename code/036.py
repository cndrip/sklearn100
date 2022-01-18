import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

filename="036.csv"
df=pd.read_csv(filename)
# df=pd.read_excel("036.xlsx")
print(df.head(3))
model =LinearRegression()
model.fit(df[["variable"]],df[["target"]])

score=model.score(df[["variable"]],df[["target"]])
print(score)