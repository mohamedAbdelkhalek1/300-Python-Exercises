"""
complex_assignment_59:

Write a Python Program to check file size. Display message if file size between 3 to 5 Mb.

"""
import os.path
file = "E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem59/file.txt"
size = os.path.getsize(file)
print(str(size)+" bytes")

size_in_Mb = size/10**6

if 5>=size_in_Mb>=3:
    print("file size between 3 to 5 Mb.")