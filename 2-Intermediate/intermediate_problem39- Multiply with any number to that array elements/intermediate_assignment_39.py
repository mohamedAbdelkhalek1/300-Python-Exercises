"""
intermediate_assignment_39:

Write a Numpy Program To Create a one-dimensional array. Display only even number from array.

"""

import numpy as np

arr = np.arange(25)

even_numbers = arr[arr % 2 == 0]

print(even_numbers)