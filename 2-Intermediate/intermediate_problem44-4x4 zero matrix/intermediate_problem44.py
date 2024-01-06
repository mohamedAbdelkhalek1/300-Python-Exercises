"""
intermediate_problem44:

Write a Python Numpy program to create a 4x4 zero matrix with elements on the main diagonal equal to 6, 7, 8, 9.   

"""

import numpy as np
arr = np.diag([6, 7, 8, 9])
print(arr)

#np.diag() : to make sqare zero array (matrix) number of index = number of rows or column and vlue that of main diagonal.