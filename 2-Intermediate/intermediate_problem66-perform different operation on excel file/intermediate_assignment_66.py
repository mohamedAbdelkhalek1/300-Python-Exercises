"""
intermediate_assignment_66:

Write a Python Program to perform arithmetic operation on excel file. 

"""

import pandas as pd
file = pd.read_excel("E:/bulding/python_exercises/2-Intermediate/intermediate_problem66-/66 Intermediate Study Materials/problem66.xlsx")
sum = 0
product = 1
subtract = 0
divide = 1
for i in file["price"]:
        sum += i
        subtract -= i
        product *= i
        divide /= i
print("Total Sum = "+str(sum))
print("Total Product = "+str(product))
print("Total subtract = "+str(subtract))
print("Total divide = "+str(divide))
