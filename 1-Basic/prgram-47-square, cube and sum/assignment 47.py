
"""
assignment 47:

Write A Python Program To Get 2 Number From The User, Find Their Cube, And Add Both Result, Finally Result Display To User.

"""


# to get 2 no
# find their Cube
# add both and display result to user

n1 = int(input("Enter 1st number "))
n2 = int(input("Enter 2nd number "))
n1_cube = n1*n1*n1
n2_cube = n2*n2*n1
print("Cube of 1st numebr is "+str(n1_cube))
print("Cube of 2nd numebr is "+str(n2_cube))
add_cube = n1_cube + n2_cube
print("Addition of both Cube is "+str(add_cube))