"""
intermediate_problem41:

Write a Python Numpy program to convert a given array into a list.

"""

import numpy as np
ar = np.array([1,2,3,4,5])
print(ar)
print(type(ar))
lst = ar.tolist()
# lst = list(ar)

print(lst)
print(type(lst))