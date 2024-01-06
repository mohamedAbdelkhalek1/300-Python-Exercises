
"""
intermediate_problem3:

Write A Python Program To Calculate Circumference And Area Of A Circle

"""

# get r 
# find cirm, area of a circle
import math
r = float(input("Enter a radius"))
# 2 pi and radius
c = 2*math.pi*r
print("Circumference of a Circle is "+str(c))

a = 2*math.pi*r*r
print("Area of a Circle is "+str(a))
