"""
complex_assignment_37:

Write a Python program to find the sequences of lowercase and UPPERCASE letters. Uppercase should be at end.

"""

import re

sent = input("Enter a sentence : ")

x = re.search('^[a-z]+[A-Z]+$', sent)

if x:
    print("Matching....")
else:
    print("Not Matching")