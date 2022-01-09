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

from sklearn.preprocessing import LabelEncoder

labelEncoder =LabelEncoder()

df["bought"]=labelEncoder.fit_transform(df["bought"])

print(df)