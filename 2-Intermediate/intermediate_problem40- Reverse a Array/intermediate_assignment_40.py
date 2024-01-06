"""
intermediate_assignment_40:

Write Python Program Convert array elements from float to integer

"""
import numpy as np
arr1 = np.array([1,2,3,4,5,6])
print(arr1)
print(arr1.dtype)

arr2 = arr1.astype(float)
print(arr2)
print(arr2.dtype)
