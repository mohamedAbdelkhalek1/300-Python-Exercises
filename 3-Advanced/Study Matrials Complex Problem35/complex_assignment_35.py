"""
complex_assignment_35:

Write a Python program to get a string from user that have starting char f and ending char z (zero, one or many z). 
Having between optional character also.

"""


import re

s = input("Enter a string")

x = re.search('^f[A-z0-9]*(z*)$' ,s)

if x:
    print("Matching....")
else:
    print("Not Matching")