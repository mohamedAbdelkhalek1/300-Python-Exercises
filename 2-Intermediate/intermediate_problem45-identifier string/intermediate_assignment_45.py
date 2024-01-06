"""
intermediate_assignment_45:

Write Python Program to make use of isidigit method with string.

You can consider that the digit string is the text that contains numbers only.

"""

digit = input("Enter a digit")

if digit.isdigit():
    print("This is a digit")
else:
    print("Not a digit")