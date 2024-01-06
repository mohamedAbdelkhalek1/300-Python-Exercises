"""
intermediate_problem65:

Write a Python Program to read specific column data from excel.

"""


import pandas as pd
col = [1,2,3]
e = pd.read_excel("E:/bulding/python_exercises/2-Intermediate/intermediate_problem65-/xlwings.xlsx", usecols=col)
print(e)
