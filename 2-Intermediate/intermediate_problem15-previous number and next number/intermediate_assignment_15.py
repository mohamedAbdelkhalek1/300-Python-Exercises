"""
intermediate_assignment_15:

Write a Python program to get a number from user to display sin and cos value of its previous number and next number.

"""
import math

n = int(input("Enter a number"))
next_n = n + 1
pre_n = n -1
print("You entered "+str(n))

print(" Sin of Previous Number is "+str(math.sin(pre_n))+ " And its Cos is "+str(math.cos(pre_n)))
print(" Sin of Previous Number is "+str(math.sin(next_n))+ " And its Cos is "+str(math.cos(next_n)))
