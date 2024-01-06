"""
intermediate_assignment_36:

Write a Python Numpy Program To Multiply Two Array.

"""

import numpy as np 

a1 = np.array([
    [1,2,3],
    [4,5,6]
])
a2 = np.array([
    [-1,-2,5],
    [8,10,-6]
])

print(a1)
print(a2)

print("Adding two array")
add_arr = np.multiply(a1,a2)
# or --> add_arr = a1 * a2
print(add_arr)