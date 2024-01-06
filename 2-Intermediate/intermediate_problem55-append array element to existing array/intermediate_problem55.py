"""
intermediate_problem55:

Write a Python Program to append array element to existing array. 

"""
from array import * 
ar = array('i',[1,2,3,4,6,5])
print(ar)
item = int(input("Enter element"))
ar.append(item)
print(ar)
