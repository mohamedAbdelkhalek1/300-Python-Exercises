
"""
problem 94:

Write Python Program To Find Force Of A Man On A Object Which Have  Mass And Acceleration. Get Mass And Acceleration From User
Formula:
	F = ma 


"""

# to get mass 
# acc
# force of a man

mass = float(input("Enter mass of an object in kg"))
acc = float(input("Enter acc of an object in m/s2"))
# F = ma
force = mass * acc
print("Mass of a object = "+str(mass)+" kg")
print("Acceleration of a object = "+str(acc)+" m/s2")
print("Force of a man = "+str(force)+" N")