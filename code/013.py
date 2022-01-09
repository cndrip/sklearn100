import pandas as pd

data_dict={
    'currency':[['PLN','USD'],
                ['EUR','USD','PLN','CAD'],
                ['GBP'],['JPY','CZK','HUF'],[]]
}

df=pd.DataFrame(data_dict)

df['number']=df["currency"].map(
    lambda x:1 if "USD" in x else 0
)

print(df)
print(df.info())