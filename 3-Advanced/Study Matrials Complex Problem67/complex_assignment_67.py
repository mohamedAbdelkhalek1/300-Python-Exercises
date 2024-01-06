"""
complex_assignment_67:

Write a Python Program to Get a string from user to find a sequence of uppercase letters having 4 length.

"""
import re

text = "adshfaSGGGBYBskl32khskl"
x = re.search("[A-Z]{4}",text)
if x:
    print("Matching...")
else:
    print("Not Matching")