"""
assignment 96:

Write A Python Program To Get 10 Float Data Type From User. System Should Convert Float Data Type Data To Integer

"""

lst = [5.5,2.1,7.6,9.5,3.4,4.4,6.5,1.8,8.8,5.9]

for i in range(len(lst)):
    lst[i] = int(lst[i])


print(lst)