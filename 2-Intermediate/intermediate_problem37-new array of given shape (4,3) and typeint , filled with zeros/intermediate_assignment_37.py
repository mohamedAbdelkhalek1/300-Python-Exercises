"""
intermediate_assignment_37:

Write a NumPy program to create a new array of given shapes (4,3) and type int , filled with ones.
And made in such a way, that the user gives shape value on run time.

"""

import numpy as np

# Get the shape from the user
rows = int(input("Enter the number of rows: "))   #4
columns = int(input("Enter the number of columns: "))     #3

# Create the array with dtype=int
new_array = np.ones((rows, columns), dtype=int)

print("New Array:")
print(new_array)