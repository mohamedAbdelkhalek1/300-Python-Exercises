"""
complex_problem29:

Write a Python program to load csv file using pandas and print the shape of the csv file and display data in the form of string.  

"""

import pandas as pd
file = pd.read_csv("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem29/myfile.csv")
print(file.shape)
print(file.to_string)