"""
intermediate_assignment_14:

Write a Python program to create a class to show concept of inheritance.

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        
    def get_salary(self):
        return self.salary
    
    
e1 = Employee("Ali", 22, 10000)
print("Name : ",e1.get_name())
print("Age : ",e1.get_age())
print("Salary : ",e1.get_salary())