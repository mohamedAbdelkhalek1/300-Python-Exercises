"""
intermediate_assignment_89:

Write a Desktop Python program to get a string from user which contain alpha at starting and ending position.

"""
import re 
text = input("Enter a string")
x = re.search('^[a-zA-Z]+.*[a-zA-Z]+$', text)
if x:
    print("Valid, start and end with number")
else:
    print("Not valid")
