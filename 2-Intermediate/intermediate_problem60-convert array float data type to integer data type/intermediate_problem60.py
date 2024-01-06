"""
intermediate_problem60:

Write a Python program to convert array float data type to integer data type.

"""


import numpy as np
ar = np.array([
    [2.3, 5.2],
    [4.1,5.3]
])
print(ar)
new_ar = ar.astype("int")
print(new_ar)