import numpy as np
import pandas as pd

df=pd.DataFrame(
    data=np.random.randn(10),
    columns=["var1"]
)
def sigmoid(x):
    return 1/(1+np.exp(-x))

# print(sigmoid(np.array([0,1,2,4])))

df["var1_sigmoid"]=df["var1"].map(sigmoid)
print(df)
