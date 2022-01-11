import numpy as np
import pandas as pd

df=pd.DataFrame({'years':[1,2,3,4,5,6],
                'salary':[4000,4250,4500,4750,5000,5250]})
# print(df)
m=len(df)
X1=df["years"].values
X=np.append(np.ones((m,1)),X1.reshape(m,1),axis=1)

print(X)
y=df["salary"]
# print(y)

v= np.dot(X.T,y)
print(v)
coefs=np.dot(np.linalg.inv(np.dot(X.T,X)),np.dot(X.T,y))
eq= f'y={coefs[0]}+{coefs[1]}x'
print(eq)

''' 
y=3749.9999999999977+249.9999999999997x
'''