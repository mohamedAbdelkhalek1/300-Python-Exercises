"""
assignment 94:

Write Python Program To Find Mass Of A Object That Accelerated By Man.

"""

force = float(input("Enter mass of an object in N"))
acc = float(input("Enter acc of an object in m/s2"))
# F = ma    , m = f/a
mass = force / acc

print("Acceleration of a object = "+str(acc)+" m/s2")
print("Force of a man = "+str(force)+" N")
print("Mass of a object = "+str(mass)+" kg")
