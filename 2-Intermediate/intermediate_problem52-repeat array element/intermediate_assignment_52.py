"""
intermediate_assignment_52:

Write a Python Numpy Program to create a one-dimensional array element. Then convert it to a list and then to a tuple. 

"""

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

lst = arr.tolist()
print(lst)

tpl = tuple(lst)
print(tpl)
