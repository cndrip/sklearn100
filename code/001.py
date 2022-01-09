import pandas as pd
import numpy as np

data = {
'size': ['XL','L','M', np.nan ,'M','M'],
'color': ['red','green','blue','green','red','green'],
'gender': ['female','male', np.nan,'female','female','male'],'price': [ 199.0 , 89.0, np.nan,129.0, 79.0, 89.0],
'weight': [ 500,450,300, np.nan, 410,np.nan ],'bought': ['yes','no','yes','no','yes','no']
}
df = pd.DataFrame(data)
print(df.isnull().sum(),len(df))

ans=np.round(df.isnull().sum()/len(df),2)
print(ans)