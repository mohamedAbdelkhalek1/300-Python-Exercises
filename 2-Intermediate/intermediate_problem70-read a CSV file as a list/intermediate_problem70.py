"""
intermediate_problem70:

Write a Python program to read a CSV file as a list

"""

import csv
file = open("E:/bulding/python_exercises/2-Intermediate/intermediate_problem70-/problem70.csv",'r')
read = csv.reader(file)
print(read)
for i in read:
    print(i)