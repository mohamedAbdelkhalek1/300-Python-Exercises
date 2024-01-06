"""
intermediate_assignment_34:

Write a Python Numpy Program to get Two Dimensional Array input from the user to Display a 2D Array using a while Loop.

"""

import numpy as np

# Get the dimensions of the array from the user
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Create an empty array of the specified dimensions
array = np.empty((rows, columns))

# Get input for each element of the array
i = 0
j = 0
while i < rows:
    while j < columns:
        element = float(input(f"Enter the element at position ({i}, {j}): "))
        array[i, j] = element
        j += 1
    i += 1
    j = 0

# Display the array
print("The 2D array is:")
i = 0
j = 0
while i < rows:
    while j < columns:
        print(array[i, j], end=" ")
        j += 1
    print()
    i += 1
    j = 0