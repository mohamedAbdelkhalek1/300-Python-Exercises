
"""
assignment 48:

Write A Python Program To Get 2 Number From The User Store In Variable, Interchange Their Value, Without Creating Temp Variable.

"""

# to get 2 numebr from the user
# store in the variables
# swaping their values

a =int( input("Enter A value"))# 5
b = int( input("Enter B value"))# 4

print("Values before swaping")
print("a = "+str(a))
print("b = "+str(b))

print("Values After swaping")

a , b = b , a         # for swap

print("a = "+str(a))
print("b = "+str(b))


