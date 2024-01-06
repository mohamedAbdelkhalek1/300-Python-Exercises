"""
intermediate_assignment_97:

Write a Python Program to get a number from user to check whether it is multiple of 5 or not using Procedural programming.

"""

"""
In Procedure Oriented programming paradigms,
series of computational steps are divided modules
which means that the code is grouped in functions and the code is serially executed step by step so basically,
it combines the serial code to instruct a computer with each step to perform a certain task.
This paradigm helps in the modularity of code and modularization is usually done by the functional implementation.
This programming paradigm helps in an easy organization related items without difficulty and so each file acts as a container.
"""

def check_multiple_of_5():
    num = int(input("Enter a number"))
    if num%5 == 0:
        print(str(num)+" is multiple by 5")
    else:
        print("Not multiple by 5")
        
check_multiple_of_5()