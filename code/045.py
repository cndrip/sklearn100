import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

df=pd.DataFrame(
    {
        "y_true":[1,0,1,2,1,0,1,1,0,1],
        "y_pred":[0,0,1,2,1,0,1,0,0,1]
    })
accuracy=accuracy_score(df["y_true"],df["y_pred"])

print(accuracy)
