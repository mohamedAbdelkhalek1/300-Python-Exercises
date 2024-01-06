"""
intermediate_assignment_53

Write a Python Program to reshape an array

"""
import numpy as np 
ar = np.array([1,2,3,4,5,6,7,8,9,10])
print(ar)

re_ar = ar.reshape(2,5)     # reshape to 2D arr with 2 row and 5 column
print(re_ar)