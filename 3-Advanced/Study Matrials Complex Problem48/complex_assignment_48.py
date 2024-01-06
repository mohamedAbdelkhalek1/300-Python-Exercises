"""
complex_assignment_48:

Write a Python Program to create an class with data members.

"""
class Employee:
    std_count = 0
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def display(self):
        print(f"Employee name {self.name}, age is {self.age}, and salary = {self.salary}")
        
e1 = Employee("Ali", 25, 7500)
e1.display()