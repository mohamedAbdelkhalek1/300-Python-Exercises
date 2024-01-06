"""
intermediate_assignment_72:

Write a Python Program to Delete cell value of CSV.

"""

import pandas as pd

file = pd.read_csv("E:/bulding/python_exercises/2-Intermediate/intermediate_problem72-/problem72.csv")

file.loc[3, "age"] = ""


file.to_csv("E:/bulding/python_exercises/2-Intermediate/intermediate_problem72-/problem72.csv")
print(file)