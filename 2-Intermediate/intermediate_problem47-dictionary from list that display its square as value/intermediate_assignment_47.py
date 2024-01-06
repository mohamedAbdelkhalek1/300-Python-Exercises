"""
intermediate_assignment_47:

Write a Python Program Create a dictionary from the list that displays its square as a key.

"""

list = [1,2,3,0,4,5,6]

dic = {i*i:i for i in list}

print(dic)
