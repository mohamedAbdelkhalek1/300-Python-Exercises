"""
complex_assignment_26:

Write a Python Program to find size of an image in MB.

"""
import os


# Get the size of the image in bytes
size_in_bytes = os.path.getsize("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem26/image.png")
# Convert the size to megabytes
size_in_mb = size_in_bytes / (1024 * 1024)

print(size_in_mb)