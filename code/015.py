import pandas as pd

df = pd.DataFrame( {
    'tags': [ '#good#vibes','#hot#summer#holiday',
              '#street#food','#workout']
})
df=df['tags'].str.split("#",expand=True)
df=df.drop(columns=[0])
df.columns=["tag1","tag2","tag3"]
df["missing"]=df.isnull().sum(axis=1)
print(df)