"""
intermediate_assignment_70:

Write a Python program to read a CSV file as a list using another method.

"""
import pandas as pd

read = pd.read_csv("E:/bulding/python_exercises/2-Intermediate/intermediate_problem70-/problem70.csv")

csv_data = read.values.tolist()       #if not use .tolist() the dt is numpy array

print(csv_data)