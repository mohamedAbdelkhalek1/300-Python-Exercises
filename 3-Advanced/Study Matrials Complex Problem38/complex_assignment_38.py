"""
complex_assignment_38:

Write a Python program that matches a string that has an ‘m or M' followed by anything, ending in ‘0 or 1'. 

"""

import re

sent = input("Enter a sentence : ")

# | means OR
x = re.search('^m|M.*0|1$', sent)

if x:
    print("Matching....")
else:
    print("Not Matching")