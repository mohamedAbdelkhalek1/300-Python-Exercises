
"""
assignment 41:


Write A Python Program To Get A Angle From The User And Find Its Sin And Cos Value In Radian 
And Then Convert Their Result Into Degree Unit


"""

import math
angle = float(input("Enter a angle in radians"))

sin_value = math.sin(angle) # in the radian
cos_value = math.cos(angle) # in the radian

# Convert the results to degrees
sin_degrees = math.degrees(sin_value)
cos_degrees = math.degrees(cos_value)

print("Sin Value = "+str(sin_value)+"rad")
print("Cos Value = "+str(cos_value)+"rad")
print("Sin Value = "+str(sin_degrees)+"degree")
print("Cos Value = "+str(cos_degrees)+"degree")