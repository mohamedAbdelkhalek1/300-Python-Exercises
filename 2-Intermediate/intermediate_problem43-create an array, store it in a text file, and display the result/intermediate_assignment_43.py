"""
intermediate_assignment_43:

Write a Python NumPy program to save a given array to a text file and load it. Using another method.

"""

# # Method 1: Using numpy.savetxt() and numpy.loadtxt()

# import numpy as np

# # Sample array
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # Save array to a text file
# np.savetxt('array.txt', arr)

# # Load array from the text file
# loaded_arr = np.loadtxt('array.txt')

# print("Loaded Array:")
# print(loaded_arr)







# Method 2: Using numpy.save() and numpy.load()

import numpy as np

# Sample array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Save array to a binary file
np.save('array.npy', arr)

# Load array from the binary file
loaded_arr = np.load('array.npy')

print("Loaded Array:")
print(loaded_arr)