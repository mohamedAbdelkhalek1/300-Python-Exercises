"""
intermediate_problem94:

Write a Python Program to remove any specific element from array. 

"""

# Remove with index
from array import *
ar = array('i',[1,10,8,13,4,5,6,7])
print(ar)
n = int(input("Enter position of element which you want to remove"))
ar.pop(n-1) #2, 3-1 = 2
print(ar)



# # Remove with value
# from array import *
# ar = array('i',[1,10,8,13,4,5,6,7])
# print(ar)
# n = int(input("Enter the element which you want to remove"))
# ar.remove(n)
# print(ar)
