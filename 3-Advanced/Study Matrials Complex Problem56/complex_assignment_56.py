"""
complex_assignment_56:

Write a Python Program to get file creation and modification date or time

"""

from os import path
import time

ct = path.getctime("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem56/myfile.csv")
ctime = time.ctime(ct)

mt = path.getmtime("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem56/myfile.csv")
mtime = time.ctime(mt)

print(ctime)

print(mtime)