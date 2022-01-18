import numpy as np
import pandas as pd

df=pd.read_csv("041.csv")

def mean_absolute_error(y_true,y_pred):
    return abs(y_true-y_pred).sum()/len(y_true)

mae=mean_absolute_error(df["y_true"],df["y_pred"])
print(mae)
