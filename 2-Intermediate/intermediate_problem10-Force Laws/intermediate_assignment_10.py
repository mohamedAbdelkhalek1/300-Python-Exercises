"""
intermediate_assignment_10:

Write A Python Program To Find Coulomb Force between two charges.

"""

#Coulomb's constant(ke), and it's equal to 8.98755 × 10⁹ N·m²/C²;
#ke = 8.98755 × 10⁹ = 
#f = (ke* (q1*q2)) / r*r
#q1— Magnitude of the first charge in Coulombs;
#q2— Magnitude of the second charge in Coulombs; and
#r— Shortest distance between the charges in meters.


q1 = float(input("Magnitude of the first charge in Coulombs"))
q2 = float(input("Magnitude of the second charge in Coulombs"))
r = float(input("Shortest distance between the charges in meters"))
product = q1 * q2 
ke = 8.98755 * 10**9
Force = (ke*(q1*q2))/r*r 
print(str(Force)+" N")