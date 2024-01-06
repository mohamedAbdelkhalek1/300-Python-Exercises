
"""
intermediate_problem74:

Write a Python Program to get column names from CSV.

"""
import csv

with open("E:/bulding/python_exercises/2-Intermediate/intermediate_problem74-/problem74.csv", 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

print(header)