"""
intermediate_problem96:

Write a Python Program to find maximum number from array.

"""

from array import *
ar = array('i',[1,10,8,13,41,5,6,7])
print(ar)
# print(max(ar))
m = ar[0]
for i in range(len(ar)):
    if m < ar[i]:
        m = ar[i]
print(m)
