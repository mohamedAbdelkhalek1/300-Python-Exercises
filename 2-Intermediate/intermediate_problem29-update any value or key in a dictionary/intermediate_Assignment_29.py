"""
intermediate_Assignment_29:

Write a Python Program to update any key in a dictionary on user request.

"""

d = {1:"Red",14:"Blue",2:"Yellow",6:"Black",9:"Green"}
print(d)
key = int(input("Enter a key, you want update"))
new_key = int(input("Enter a new key"))
d[new_key] = d[key]
d.pop(key)
print(d)
# but new item append at the end 