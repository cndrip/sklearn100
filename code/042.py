import numpy as np
import pandas as pd

df=pd.read_csv(r"E:\bigdata\sklearn100\code\041.csv")

def mean_squared_error(y_true,y_pred):
    return ((y_true-y_pred)**2).sum()/len(y_true)

mae=mean_squared_error(df["y_true"],df["y_pred"])
print(mae)
