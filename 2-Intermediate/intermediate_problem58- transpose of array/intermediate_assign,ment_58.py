"""
intermediate_assign,ment_58:

Write a Python Pandas program to compare two Numpy array.

"""

import numpy as np
import pandas as pd

arr1 = np.array([2,4,6,8])
arr2 = np.array([1,3,5,7])

df1 = pd.DataFrame(arr1)
df2 = pd.DataFrame(arr2)

# Compare the arrays
comparison = df1 == df2
print(comparison)