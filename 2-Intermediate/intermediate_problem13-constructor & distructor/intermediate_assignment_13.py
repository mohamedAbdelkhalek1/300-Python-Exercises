"""
intermediate_assignment_13:

Write a Python program to create a destructor.

"""

# Python program to illustrate destructor
class Employee:
 
    # Initializing
    def __init__(self):
        print('Employee created.')
 
    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')
 
obj = Employee()
del obj

#Output:
# Employee created.
# Destructor called, Employee deleted.