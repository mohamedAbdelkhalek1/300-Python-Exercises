"""
intermediate_assignment_96:

Write a Python Program to find the minimum number from the array.

"""
from array import *
ar = array('i',[1,10,8,13,41,5,6,7])
print(ar)
# print(min(ar))
m = ar[0]
for i in range(len(ar)):
    if m > ar[i]:
        m = ar[i]
print(m)
