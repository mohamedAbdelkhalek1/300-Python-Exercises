
"""
intermediate_problem48:

Write a Python Program to Create a list from an existing list that counts numbers less than 20 greater than 5.

"""

list = [1,2,3,4,20,21,24,4,5,8,9,10,18,19]

new_list = [i for i in list if i < 20 if i > 5]
print(new_list)

count = len(new_list)

print(count)