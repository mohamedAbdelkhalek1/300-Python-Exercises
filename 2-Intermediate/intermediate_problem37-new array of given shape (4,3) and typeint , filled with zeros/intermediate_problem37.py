"""
intermediate_problem37:

Write a NumPy program to create a new array of given shape (4,3) and typeint , filled with zeros. 

"""

import numpy as np
# ar = np.zeros( (4,3))   #float
ar = np.zeros( (4,3), dtype=np.int64)  #int
print(ar)