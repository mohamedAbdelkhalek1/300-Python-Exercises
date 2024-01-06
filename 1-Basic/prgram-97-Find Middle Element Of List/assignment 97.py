"""
assignment 97:

Write A Python Program To Find Square Root Of Middle Element Of List Items

"""
import math

lst = [4,5,9,4,2]

half = int(len(lst)/2)

middle_el = lst[half]

print("Middle Element = "+str(middle_el))

print(" Square Root Of Middle Element = "+str(math.sqrt(middle_el)))