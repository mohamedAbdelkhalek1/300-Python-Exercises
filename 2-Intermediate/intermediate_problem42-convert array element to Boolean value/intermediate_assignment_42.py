"""
intermediate_problem42:

Write a Python NumPy program to convert an array to bytes and load it as array.

"""


import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])

# Convert array to bytes
bytes_data = arr.tobytes()

# Load bytes as array
loaded_array = np.frombuffer(bytes_data, dtype=arr.dtype)

print("Original Array:")
print(arr)

print("Loaded Array:")
print(loaded_array)