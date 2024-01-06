"""
intermediate_assignment_73:

Write a Python Program to delete any row in a CSV file

"""

import pandas as pd

file = pd.read_csv("E:/bulding/python_exercises/2-Intermediate/intermediate_problem73-/73 Intermediate Study Materials/problem72.csv")

file.drop(1, inplace=True)


file.to_csv("E:/bulding/python_exercises/2-Intermediate/intermediate_problem73-/73 Intermediate Study Materials/problem72.csv")
print(file)