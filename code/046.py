import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix

df=pd.DataFrame(
    {
        "y_true":[1,0,1,2,1,0,1,1,0,1,1,0,0],
        "y_pred":[0,0,1,2,1,0,1,0,0,1,0,1,1]
    })
cm=confusion_matrix(df["y_true"],df["y_pred"])

print(cm)
