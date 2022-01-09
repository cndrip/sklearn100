import pandas as pd

df = pd.DataFrame( {
'investments' :['100_000_000','100_000',
                '30_000_000','100_500_000']
})

df["investments"]=df["investments"].str.replace("_","").astype(int)

print(df)