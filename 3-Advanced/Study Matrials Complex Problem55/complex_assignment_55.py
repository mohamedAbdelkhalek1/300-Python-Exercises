"""
complex_assignment_55:

Write a Python Program to print the memory usage of List.

"""

import sys

lst = [5,14,"Ali",True]

size = sys.getsizeof(lst)

print("Size of the list = ",size)