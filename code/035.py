import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df=pd.DataFrame({'years':[1,2,3,4,5,6],
                'salary':[4000,4250,4500,4750,5000,5250]})

model = LinearRegression()
model.fit(
    df[['years']],
    df[['salary']]
)
print(model.intercept_, model.coef_)

f"y={model.intercept_[0]} + {model.coef_[0]}x"

# print(df)
