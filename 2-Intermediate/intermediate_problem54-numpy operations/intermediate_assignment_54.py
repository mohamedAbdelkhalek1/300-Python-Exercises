"""
intermediate_assignment_54:

Write a Python Numpy Program to display  1-dimensional array with equality gaps between a range.

"""

import numpy as np
# ar = np.arange(1,15,2)    #array from 1 to 15 with gap 2
# print(ar)



# another solution can get start, end and number of item that you want and return double items
array = np.linspace(1, 15, 5)
print(array)