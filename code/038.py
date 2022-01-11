import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

df = pd.DataFrame({
    "x":np.arange(10),
    "y":np.arange(10,20)
})
poly=PolynomialFeatures(degree=2)

df_poly = poly.fit_transform(df)
print(df_poly)
'''
[[  1.   0.  10.   0.   0. 100.]
 [  1.   1.  11.   1.  11. 121.]
 [  1.   2.  12.   4.  24. 144.]
 [  1.   3.  13.   9.  39. 169.]
 [  1.   4.  14.  16.  56. 196.]
 [  1.   5.  15.  25.  75. 225.]
 [  1.   6.  16.  36.  96. 256.]
 [  1.   7.  17.  49. 119. 289.]
 [  1.   8.  18.  64. 144. 324.]
 [  1.   9.  19.  81. 171. 361.]]
'''