"""
assignment 93:

Write A Python Program To Find Time Taken By An Object Having Velocity difference ‘dv‘ And ‘a’ Acceleration.
Get Velocity And Acceleration From The User

"""

# acc = delta v /t   ,    t = dv/acc

vi = float(input("Enter vi in m/s"))
vf = float(input("Enter vf in m/s"))
acc = float(input("Enter Acceleration in m/s2"))
change_velocity = vf-vi
t = change_velocity / acc
print("time of an obejct = "+str(t)+" s")