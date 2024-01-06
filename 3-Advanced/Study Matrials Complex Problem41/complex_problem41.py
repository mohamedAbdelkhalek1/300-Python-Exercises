"""
complex_problem41:

Write a Python program which match a string that contains uppercase,  lowercase char, numbers, and underscores. 
It Ignore white space, punctuation etc

"""

import re

str = input("Enter a str")

# uppercase, lowercase, number and underscore   (in the same sort)
x = re.search('[A-Z]+[a-z]+[0-9]+[_]+', str)

# # uppercase, lowercase, number and underscore   (not sorted)
# x = re.search('^[A-Za-z0-9_]$', str)
# #or
# x = re.search('^\w$', str)

if x:
    print("Matching....")
else:
    print("Not Matching")