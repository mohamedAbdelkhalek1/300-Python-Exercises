"""
assignment 91:

Write A Python Program Find A Mass Of An Object Through Density 

"""

# d = m / v, m = d*v

d = int(input("Write a Density of the object"))
v = int(input("Write a volume of the object"))

m = d * v


print("Volume = "+str(v)+" cm3")
print("Density = "+str(d)+" g/cm3")

print("Mass = "+str(m)+" gram")

