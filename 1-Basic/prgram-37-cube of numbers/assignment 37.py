
"""
assignment 37:

Write A Python Program To Get 6 Number From The User To Find The Square Of First Three Number And Find Cube Of Next Three Number

"""
# Take 6 numbers as input from user
print("Enter 6 Number To Find The Square Of First Three Number And Find Cube Of Next Three Number ")
numbers = []
for i in range(6):
    numbers.append(int(input(f"Enter number {i+1}: ")))
    
# Find square of first 3 number
print("Square of first 3 numbers:")
for i in range(3):
    print(f"Square of number {i+1} = {numbers[i]**2}")
    
# Find cube of next 3 numbers
print("cube of next 3 numbers:")
for i in range(3,6):
    print(f"Square of number {i+1} = {numbers[i]**3}")