import numpy as np
import pandas as pd

df=pd.DataFrame(
    {
        "var_1":np.arange(0.01,1,0.1),
        "var_2":1-np.arange(0.01,1,0.1)
    }
)

def entropy(x):
    return -np.sum(x*np.log2(x))

df["entropy"]=df.apply(
    lambda x: entropy([x["var_1"],x["var_2"]]),
    axis=1
)
print(df)
'''
   var_1  var_2   entropy
0   0.01   0.99  0.080793
1   0.11   0.89  0.499916
2   0.21   0.79  0.741483
3   0.31   0.69  0.893173
4   0.41   0.59  0.976500
5   0.51   0.49  0.999711
6   0.61   0.39  0.964800
7   0.71   0.29  0.868721
8   0.81   0.19  0.701471
9   0.91   0.09  0.436470
'''
