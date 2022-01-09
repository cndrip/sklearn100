import pandas as pd

df=pd.DataFrame(data={'weight':[75.,78.5,85.,91.,84.5,83.,68.]})
df['weight_cut']=pd.cut(df['weight'],bins=[60,75,80,95])
print(df)
print(df.info())