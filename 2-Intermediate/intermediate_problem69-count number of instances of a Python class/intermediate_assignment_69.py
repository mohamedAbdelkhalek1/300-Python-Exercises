"""
intermediate_assignment_69:

Write a Python Program to count number of instances of a Python class. Use another Method.

"""
class MyClass:
    count = 0  # class variable to keep track of the count

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_instance_count(cls):
        return cls.count

# Creating instances of MyClass
obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

# Printing the count of instances
print("Number of instances:", MyClass.get_instance_count())