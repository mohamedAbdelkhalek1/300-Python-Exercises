
"""
intermediate_problem66:

Write a Python Program to perform different operation on excel file

"""

import pandas as pd
file = pd.read_excel("E:/bulding/python_exercises/2-Intermediate/intermediate_problem66-/66 Intermediate Study Materials/problem66.xlsx")
sum = file["price"].sum()
product = file["price"].product()
count = file["price"].count()
mean = file["price"].mean()
print("Total Sum = "+str(sum))
print("Total Product = "+str(product))
print("Total Values = "+str(count))
print("Total Mean = "+str(mean))
