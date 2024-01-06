"""
complex_assignment_40:

Write a Python program that matches a word containing ‘6‘ digit.  

"""
import re

w = input("Enter a word")


x = re.search('6', w)

if x:
    print("Matching....")
else:
    print("Not Matching")