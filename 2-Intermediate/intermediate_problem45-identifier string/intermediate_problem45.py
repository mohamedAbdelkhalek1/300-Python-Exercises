
"""
intermediate_problem45:

Write a Python Program to make use of isidentifier method with string

You can consider that the identifier string is the text that can be the name of a variable.

"""

identifier = input("Enter a identifier")

if identifier.isidentifier():
    print("This is valid identifier")
else:
    print("Not a valid")
    