"""
complex_assignment_22:

Create  a Python Program to Count total number of Uppercase , Lowercase and digits in a string. 

"""
s = input("Enter a string")
u = 0
l = 0
d = 0

for i in s:
    if i.isupper():
        u += 1
    if i.islower():
        l += 1
    if i.isdigit():
        d += 1
print("Total numebr of uppercase = "+str(u))
print("Total numebr of Lowercase = "+str(l))
print("Total numebr of Digits = "+str(d))