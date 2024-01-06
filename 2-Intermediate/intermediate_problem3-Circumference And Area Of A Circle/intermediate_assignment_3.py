"""
intermediate_assignment_3:

Write A Python Program To Calculate the Circumference And Area Of A Circle.
Half The Answer Of Circumference And Area Circle Then Add Both Results, Finally Display To User As Result

"""

import math
r = float(input("Enter a radius"))

c = 2*math.pi*r
print("Circumference of a Circle is "+str(c))

a = 2*math.pi*r*r
print("Area of a Circle is "+str(a))

print(f"Half The Answer Of Circumference And Area Circle = {c/2 + a/2}")