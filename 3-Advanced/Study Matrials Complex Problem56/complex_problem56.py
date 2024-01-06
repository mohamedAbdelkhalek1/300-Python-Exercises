"""
complex_problem56:

Write a Python Program to get file creation date or time

"""

from os import path
import time

t = path.getctime("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem56/myfile.csv")
ctime = time.ctime(t)
print(ctime)