"""
intermediate_assignment_57:

Write a Python Pandas program to convert a Pandas series to Numpy array.

"""

import numpy as np
import pandas as pd

ps = pd.Series([1,2,3,4,5,6,7])
print(ps)

arr = np.array(ps)
print(arr)