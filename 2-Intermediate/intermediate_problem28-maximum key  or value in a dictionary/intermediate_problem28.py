"""
intermediate_problem28:

Write a Python Program to find a maximum key in a dictionary (having key with number data type)

"""

d = {1:"Red",14:"Blue",2:"Yellow",6:"Black",9:"Green"}
print(d)
keys = list(d.keys())
print("Max key in a dic is = "+str(max(keys))) 

# keys.sort()
# print(keys)
# print("Max key in a dic is = "+str(keys[-1])) 
