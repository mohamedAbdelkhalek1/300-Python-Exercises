"""
complex_assignment_39:

Write a Python program to check a to z, A- Z, 0 to 9 and _ from a user entered string at ENDING position.

"""
import re

sent = input("Enter a sentence")

x = re.search('\w+$', sent)

if x:
    print("Matching....")
else:
    print("Not Matching")