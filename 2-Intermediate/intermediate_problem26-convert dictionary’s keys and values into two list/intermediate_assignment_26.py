"""
intermediate_assignment_26:

Write a Python program to convert dictionary’s keys and values into two tuple.
One tuple should store keys and other tuple should store values.

"""
d = {1:"Red",2:"Blue",3:"Yellow",4:"Black",5:"Green"}
print(d)
keys = []
values = []

for key, value in d.items():
    keys.append(key)
    values.append(value)

keys_tuple = tuple(keys)
values_tuple = tuple(values)

print(keys_tuple)
print(values_tuple)







# #Another solution
# d = {1:"Red",2:"Blue",3:"Yellow",4:"Black",5:"Green"}
# key = tuple(d.keys())
# print(key)
# value = tuple(d.values())
# print(value)