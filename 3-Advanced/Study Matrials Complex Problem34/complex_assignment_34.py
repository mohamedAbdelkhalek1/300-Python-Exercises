"""
complex_assignment_34:

Write a Python Program to get a alpha character from user to check whether it is in given range or not: range(a to f) or (A-F)

"""

import re
# a to f

s = input("Enter a char : ")
x = re.search('[a-fA-F]', s)
if x:
    print("Matching...")
else:
    print("Not Matching...")