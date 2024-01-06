"""
complex_assignment 1:

Write a Python Program To Find Roots Of Quadratic Equation: Make some modification

"""
print("Quadratic Equation : ax^2 + bx + c")

a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
c = float(input("Enter the value of c : "))

if a == 0:
    print(f"There is a linear equation and X = {-c/b}")
else:
    r = b**2-4*a*c
    if r > 0:
        x1 = (-b + r**0.5)/2*a
        x2 = (-b - r**0.5)/2*a
        print(x1,x2)
        print("There are two roots")
    elif r == 0:
        x = -b/2*a
        print("There is one root")
    else:
        print("No roots")