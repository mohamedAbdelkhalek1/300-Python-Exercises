
"""
intermediate_problem10:

Write A Python Program To Find Gravitational Force

"""


# G =  6.6743 × 10^-11 = 0.00000000006674
# F = (G*(m1*m2))/r*r 

m1 = float(input("Mass of object 1"))
m2 = float(input("Mass of object 2"))
r = float(input("Enter radius"))
product = m1 * m2 
G = 0.00000000006674
Force = (G*(m1*m2))/r*r 
print(str(Force)+" N")
