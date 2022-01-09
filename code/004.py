import pandas as pd
import numpy as np
from sklearn import impute

data = {
'size': ['XL','L','M', np.nan ,'M','M'],
'color': ['red','green','blue','green','red','green'],
'gender': ['female','male', np.nan,'female','female','male'],
'price': [ 199.0 , 89.0, np.nan,129.0, 79.0, 89.0],
'weight': [ 500,450,300, np.nan, 410,np.nan ],
'bought': ['yes','no','yes','no','yes','no']
}
df = pd.DataFrame(data)
from sklearn.impute import SimpleImputer

# imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer = SimpleImputer(
    missing_values=np.nan, 
    strategy="constant",
    fill_value=99.0
)
df[["price"]]=imputer.fit_transform(df[["price"]])

print(df)