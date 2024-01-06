
"""
intermediate_assignment_11:

Write A Python Program To Get a length in cm and convert to m and km

"""


cm = float(input("Enter a length in cm"))
# 1cm = 0.01 m
# 1cm = 0.00001 km

m = cm * 0.01
km = cm * 0.00001

print("Cm "+str(cm)+" is converted into " +str(m)+" meters")
print("Cm "+str(cm)+" is converted into " +str(km)+" kilo meters")