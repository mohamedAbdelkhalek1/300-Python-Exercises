"""
intermediate_assignment_74:

Write a Python Program to get column names from CSV. Using another method.

"""

import pandas as pd
file = pd.read_csv("E:/bulding/python_exercises/2-Intermediate/intermediate_problem74-/problem74.csv")

file_col = file.index[0]
print(file_col)
