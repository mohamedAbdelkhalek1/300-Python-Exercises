"""
intermediate_assignment_41:

Write a Python Numpy program to convert a given list into an array, then again convert it into a list. 

"""
import numpy as np
lst = [1,2,3,4,5]
ar = np.array(lst)
print(ar)
print(type(ar)) 

lst = ar.tolist()
print(lst)
print(type(lst))