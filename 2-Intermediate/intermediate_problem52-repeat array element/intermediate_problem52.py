
"""
intermediate_problem52:

Write a Python Numpy Program to repeat array element.

"""


import numpy as np
ar = np.array([1,2,3,4,5])
print(ar)
n = int(input("Enter a number"))
r_ar = np.tile(ar, n)
print(r_ar)