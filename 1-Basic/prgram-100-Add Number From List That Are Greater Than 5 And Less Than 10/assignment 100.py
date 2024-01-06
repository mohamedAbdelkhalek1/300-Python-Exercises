"""
assignment 100:

Write A Python Program To Add Even Number From List

"""

lst = [1,3,1.3,5,10,7,7,4,8,9,50,43] 
s = 0
for i in lst:
    if(i %2 ==0):   
        s += i
print(s)