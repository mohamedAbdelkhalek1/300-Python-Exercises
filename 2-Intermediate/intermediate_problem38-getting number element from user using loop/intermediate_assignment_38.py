"""
intermediate_assignment_38:

Write a NumPy program to create one-dimensional array, getting number element from user using while loop.

"""

import numpy as np

num = int(input("Enter a number of elements")) # 6
ar = np.zeros(num, dtype=np.int64) # 6
i= 0
while i < num:
    element = int(input(f"Enter array element {i+1} : "))
    ar[i] = element
    i+=1
    
print(ar)