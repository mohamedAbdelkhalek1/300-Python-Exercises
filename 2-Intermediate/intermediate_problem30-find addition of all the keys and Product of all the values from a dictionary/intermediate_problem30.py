"""
intermediate_problem30:

Write a Python Program to Create a Dictionary to find addition of all the keys and Product of all the values from a dictionary.

"""

# d = {1:100,14:14000,2:2000,6:6000,9:9000}
# print(d)

# keys = []
# for k in d.keys():
#     keys.append(k)
# print(keys)
# addition = 0
# for i in keys:
#     addition += i
# print(addition)

# values = []
# for v in d.values():
#     values.append(v)
# print(values)
# product = 1
# for i in values:
#     product *= i
# print(product)



# Another solution:
from math import prod

d = {1:100,14:14000,2:2000,6:6000,9:9000}
print(d)

keys = list(d.keys())
key_sum = sum(keys)
print(key_sum)

values = list(d.values())
value_product = prod(values)
print(value_product)
