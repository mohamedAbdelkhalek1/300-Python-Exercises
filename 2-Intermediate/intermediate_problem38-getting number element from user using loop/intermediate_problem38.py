
"""
intermediate_problem38:

Write a NumPy program to create one-dimensional array, getting number element from user using for loop.

"""

import numpy as np
num = int(input("Enter a number of elements")) # 6
ar = np.zeros(num, dtype=np.int64) # 6

for i in range(len(ar)):
    element = int(input(f"Enter array element {i+1} : "))
    ar[i] = element
print(ar)