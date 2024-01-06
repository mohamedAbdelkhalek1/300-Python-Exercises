"""
intermediate_problem57:

Write a Python Pandas program to convert a Numpy array to a Pandas series.

"""

import numpy as np
import pandas as pd

ar = np.array([1,2,3,4,5,6,7])
index = [i for i in range(10,17)]
print(ar)
ps = pd.Series(ar,index)
print(ps)