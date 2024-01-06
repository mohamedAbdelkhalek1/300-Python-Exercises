"""
complex_problem59:

Write a Python Program to check file size.

"""

import os.path
file = "E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem59/file.txt"
size = os.path.getsize(file)
print(str(size)+" bytes")