"""
assignment 84:

Write A Python Program To Get Name From User, To Check It Is In Lowercase Or Not, If Not Lowercase Then Convert Into Lowercase

"""

#lovercase means all char is lower


name = input("Enter your name")

if(name.islower()):
    print("Name is already in Lowercase "+name)
else:
    print("name is converted to Lowercase that is "+name.lower())
    
    
