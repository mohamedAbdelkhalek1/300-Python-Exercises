"""
problem 84:

Write A Python Program To Get Name From User, To Check It Is In Uppercase Or Not, If Not Upper Then Convert Into Uppercase

"""
#Upper case means all char is upper
#but capitalize means first char is capital and all is small


# to get name
# convert to uppercase if not
# display to user

name = input("Enter your name")

if(name.isupper()):
    print("Name is already in uppercase "+name)
else:
    print(" name is converted to uppercase that is "+name.upper())