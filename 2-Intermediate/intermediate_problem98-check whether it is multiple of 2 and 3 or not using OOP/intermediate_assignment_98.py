"""
intermediate_assignment_98:

Write a Python Program to get a number from user to check whether it is multiple of 2 and 3 or not using Procedural programming.

"""

def check_multiple_of_2_and_3():
    num = int(input("Enter a number"))
    if num%2 == 0 and num%3 == 0:
        print(str(num)+" is multiple by 5")
    else:
        print("Not multiple by 5")
        
check_multiple_of_2_and_3()