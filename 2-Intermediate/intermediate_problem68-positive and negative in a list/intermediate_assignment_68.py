"""
intermediate_assignment_68:

Write a Python Program to display positive, negative and Zero in a list.
When there is positive, negative or Zero number. Using list comprehension.

"""

lst = [1,2,3,0,-4,5,-3,0,9,-8]

print(lst)

new_list = [ "Positive" if i > 0 else "Zero" if i==0 else "Negative" for i in lst]

print(new_list)