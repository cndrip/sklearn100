import pandas as pd

data = {
'size': ['XL','L','M', 'L','M'],
'color': ['red','green','blue','green','red'],
'gender': ['female','male', 'male','female','female'],
'price': [ 199.0 , 89.0,99,129.0, 79.0],
'weight': [ 500,450,300, 380, 410 ],
'bought': ['yes','no','yes','no','yes']
}
df=pd.DataFrame(data=data)

# from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

oneHotEncoder =OneHotEncoder(sparse=False)

# oneHotEncoder.fit(df[["size"]])
# print(oneHotEncoder.transform(df[["size"]]))

print(oneHotEncoder.fit_transform(df[["size"]]))
print(oneHotEncoder.categories_)