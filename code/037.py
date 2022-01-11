import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

df = pd.DataFrame(
    data=np.arange(10),
    columns=['x']
)
poly=PolynomialFeatures(degree=2)

df_poly = poly.fit_transform(df)
print(df_poly)
'''
[[ 1.  0.  0.]
 [ 1.  1.  1.]
 [ 1.  2.  4.]
 [ 1.  3.  9.]
 [ 1.  4. 16.]
 [ 1.  5. 25.]
 [ 1.  6. 36.]
 [ 1.  7. 49.]
 [ 1.  8. 64.]
 [ 1.  9. 81.]]
'''