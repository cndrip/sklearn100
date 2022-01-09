import pandas as pd

data_dict={
    'currency':[['PLN','USD'],
                ['EUR','USD','PLN','CAD'],
                ['GBP'],['JPY','CZK','HUF'],[]]
}

df=pd.DataFrame(data_dict)

df['number']=df["currency"].map(len)

print(df)
print(df.info())