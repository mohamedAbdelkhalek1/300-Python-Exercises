"""
complex_assignment_43:

Write a Python program to match a number and _ at the ending of a string.  

"""
import re

str = input("Enter a str")

# String end with number (0 to 5)
x = re.search('[0-9_]+$', str)

if x:
    print("Matching....")
else:
    print("Not Matching")