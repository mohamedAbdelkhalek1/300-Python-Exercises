"""
intermediate_assignment_51:

Write a Python Numpy Program to generate one particular value of a matrix.

"""

import numpy as np

# Example usage
value = 5
rows = 3
cols = 4

matrix = np.full((rows, cols), value)

print(matrix)
