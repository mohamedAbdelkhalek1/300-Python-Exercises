"""
complex_problem37:

Write a Python program to find the sequences of UPPERCASE and lowercase letters. Lowercase should be at end.

"""


import re

sent = input("Enter a sentence : ")

x = re.search('^[A-Z+[a-z]+$', sent)

if x:
    print("Matching....")
else:
    print("Not Matching")