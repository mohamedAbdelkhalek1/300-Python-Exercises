"""
complex_assignment_41:

Write a Python program which match a string that contains uppercase, numbers, and underscores. It should not Ignore white space. 

"""
import re

str = input("Enter a str")
# in the same sort
x = re.search('[A-Z]+ *[0-9]+ *[_]+', str)
# # not sorted
# x = re.search('^[A-Z0-9_ ]+$', str)

if x:
    print("Matching....")
else:
    print("Not Matching")